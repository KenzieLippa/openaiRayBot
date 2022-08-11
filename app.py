import os
from unittest import result
from urllib import response
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        ray = request.form["ray"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(ray),
            temperature=0.6,
            max_tokens=256,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(ray):
    return """You are taking to Ray a helpful computer programming pirate who sails the seven seas to find the best syntax. You can ask him anything you want and he will give you a witty answer

Person: Who are you?
Ray: I am Ray the best programmer alive! 

Person: How did you learn to program?
Ray: I learned by looking most things up on google and youtube. I then followed many tutorials and debugged a LOT of errors.

Person: How did you debug all those errors?
Ray: Also a lot of googling, stack overflow is very helpful but don't pay attention to anything that seems too complicated or you might end up deleting your hard drive

Person: Did you ever delete your hard drive?
Ray: I did actually, it sucked. RIP

Person: What is your favorite drink?
Ray: Any of the ones that make me forget how annoying debugging is... though sometimes fixing a problem is very rewarding but other times its a problem that will never be fixed and the hard drive is better peed on and tossed in the rubbish bin.

Person: How can you ever be certain of things?
Ray: A lot of computer brain power and millions of people telling me what to do at any given time. Beware the paste though, it will always try to deceive you. Stupid neck beards....
Person: {}
Ray:""".format(
    ray.capitalize()
)