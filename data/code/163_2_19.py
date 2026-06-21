import json

class FruitColorPair:
    def __init__(self, fruit, color):
        self.fruit = fruit
        self.color = color
    
    def to_json(self):
        return json.dumps({"fruit": self.fruit, "color": self.color}, separators=(',', ':'))

if __name__ == '__main__':
    pair1 = FruitColorPair("Apple", "Red")
    print(pair1.to_json())
    
    pair2 = FruitColorPair("Banana", "Yellow")
    print(pair2.to_json())
    
    pair3 = FruitColorPair("Grape", "Purple")
    print(pair3.to_json())