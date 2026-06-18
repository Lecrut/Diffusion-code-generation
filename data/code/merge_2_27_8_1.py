import json
class FruitClassifier:
    def __init__(self):
        self.config = {
            "categories": [
                {"name": "citrus", "keywords": ["orange", "lemon", "lime"]},
                {"name": "berries", "keywords": ["strawberry", "blueberry", "raspberry"]},
                {"name": "tropical", "keywords": ["mango", "pineapple", "papaya"]}
            ]
        }
    def classify(self, fruit_name):
        normalized = fruit_name.lower().strip()
        for category in self.config["categories"]:
            if any(keyword in normalized for keyword in category["keywords"]):
                return {"fruit": fruit_name, "category": category["name"]}
        return {"error": f"Unknown fruit: {fruit_name}"}
    def add_category(self, name, keywords):
        self.config["categories"].append({"name": name, "keywords": [k.lower() for k in keywords]})
def load_config_from_file(filepath):
    with open(filepath) as f:
        return json.load(f)["categories"]
if __name__ == '__main__':
    classifier = FruitClassifier()
    test_fruits = ["Orange", "Strawberry", "Mango", "Banana", "Lemon"]
    for fruit in test_fruits:
        result = classifier.classify(fruit)
        print(result)