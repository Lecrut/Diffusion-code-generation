import json
class FruitClassifier:
    def __init__(self):
        self.classification_rules = {
            "red": ["apple", "strawberry"],
            "citrus": ["orange", "lemon"],
            "stone_fruit": ["peach", "plum"]
        }
    def classify(self, fruit_name: str) -> dict | None:
        for category in self.classification_rules.keys():
            if fruit_name.lower() in [item.lower() for item in self.classification_rules[category]]:
                return {"name": fruit_name, "category": category}
        return None
    def add_rule(self, category: str, items: list[str]):
        self.classification_rules[category] = [item.lower() for item in items]
if __name__ == '__main__':
    classifier = FruitClassifier()
    test_fruits = ["Apple", "Banana", "Orange", "Grape"]
    results = []
    for fruit in test_fruits:
        result = classifier.classify(fruit)
        if result:
            results.append(result)
    output_data = {
        "classifications": results,
        "rules_configured": list(classifier.classification_rules.keys())
    }
    print(json.dumps(output_data))