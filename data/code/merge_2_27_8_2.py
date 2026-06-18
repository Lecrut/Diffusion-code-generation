import json
class FruitClassifier:
    def __init__(self):
        self.classification_rules = {
            "citrus": ["orange", "lemon", "lime"],
            "berry": ["strawberry", "blueberry", "raspberry"],
            "stone": ["peach", "plum", "apricot"]
        }
    def classify(self, fruit_name):
        for category in self.classification_rules:
            if fruit_name.lower() in [f.lower() for f in self.classification_rules[category]]:
                return category
        return None
def load_config(config_path="config.json"):
    with open(config_path) as file:
        config = json.load(file)
    rules = {}
    for cat, items in config.items():
        if isinstance(items, list):
            rules[cat] = [item.lower() for item in items]
    return rules
def main():
    sample_fruits = ["orange", "strawberry", "banana"]
    classifier = FruitClassifier()
    results = {}
    for fruit in sample_fruits:
        category = classifier.classify(fruit)
        if category is not None:
            results[fruit] = category
    print(json.dumps(results, indent=2))
if __name__ == '__main__':
    main()