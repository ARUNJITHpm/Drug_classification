from  flask import Flask

application = Flask(__name__)


@application.route('/hi/',methods=['GET'])
def home():
    return '<h1>This is my home page</h1>'



if __name__=='__main__':
    application.run(debug=True)