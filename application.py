import os
from flask import Flask

application = Flask(__name__)


@application.route("/")
def home():
    environment = os.getenv("APP_ENV", "development")
    version = os.getenv("APP_VERSION", "1.0")
    return f"""
    <h1>AWS CI/CD - Assignment 4</h1>
    <h2>Elastic Beanstalk Flask Application</h2>
    <p>Environment: {environment}</p>
    <p>Version: {version}</p>
    <p>Deployed using AWS CodePipeline.</p>
    """


@application.route("/health")
def health():
    return {
        "status": "healthy",
        "environment": os.getenv("APP_ENV", "development"),
        "version": os.getenv("APP_VERSION", "1.0"),
    }


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000)
