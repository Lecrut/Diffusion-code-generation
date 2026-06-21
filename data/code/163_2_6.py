import json

class FruitColorGenerator:
    def __init__(self):
        self.pairs = [
            {"fruit": "apple", "color": "red"},
            {"fruit": "banana", "color": "yellow"},
            {"fruit": "grape", "color": "purple"}
        ]
    
    @staticmethod
    def to_json(data):
        return json.dumps(data, separators=(',', ':'))

if __name__ == '__main__':
    generator = FruitColorGenerator()
    json_output = FruitColorGenerator.to_json(generator.pairs)
    print(json_output)