#!/usr/bin/env python3


from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy pickleball player data
players = [
    {"id": 1, "name": "John", "rating": 4.5, "city": "New York"},
    {"id": 2, "name": "Alice", "rating": 4.2, "city": "Los Angeles"}
]

# API endpoint for fetching all players
@app.route('/api/players', methods=['GET'])
def get_players():
    return jsonify(players)

# API endpoint for filtering players by city
@app.route('/api/players/filter', methods=['GET'])
def filter_players():
    city = request.args.get('city')
    filtered_players = [player for player in players if player['city'] == city]
    return jsonify(filtered_players)

# Add more endpoints for CRUD operations, filtering, and authentication

if __name__ == '__main__':
    app.run(debug=True)
