import json

class FruitColor:
    def __init__(self, fruit: str, color: str):
        self.fruit = fruit
        self.color = color

    def to_dict(self) -> dict:
        return {"fruit": self.fruit, "color": self.color}

if __name__ == '__main__':
    apple = FruitColor("Apple", "Red")
    banana = FruitColor("Banana", "Yellow")
    grapes = FruitColor("Grape", "Purple")

    fruit_color_list = [apple.to_dict(), banana.to_dict(), grapes.to_dict()]
    
    json_output = json.dumps(fruit_color_list, separators=(',', ':'))
    print(json_output)