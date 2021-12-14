from flask import Flask, request, jsonify
import Util

app = Flask(__name__)

@app.route('/get_location_name')
def get_locations():
    response = jsonify({
        'location' : Util.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':

    print('Starting Python flask server for Home Price Prediction')
    app.run()