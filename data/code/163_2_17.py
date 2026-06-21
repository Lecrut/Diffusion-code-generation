import json

class FruitColorPair:
    def __init__(self, fruit, color):
        self.fruit = fruit
        self.color = color
    
    def to_dict(self):
        return {"fruit": self.fruit, "color": self.color}

if __name__ == '__main__':
    pair1 = FruitColorPair("Apple", "Red")
    pair2 = FruitColorPair("Banana", "Yellow")
    pair3 = FruitColorPair("Grape", "Purple")
    
    fruit_color_list = [pair1.to_dict(), pair2.to_dict(), pair3.to_dict()]
    json_output = json.dumps(fruit_color_list, separators=(',', ':'))
    print(json_output)