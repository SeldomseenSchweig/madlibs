from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)

app.config['SECRET_KEY'] = "hayduke"
debug = DebugToolbarExtension(app)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")


@app.route('/')
def make_madlib_template():
    
    words =  story.prompts
    return render_template('home.html', words=words)

@app.route('/story')
def fill_madlib():
    story_dict = {}
    for prompt in story.prompts:
       story_dict[prompt] = request.args[prompt]
       
    text = story.generate(story_dict)
    
    
    return render_template('story.html', text=text)
    



