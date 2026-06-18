import json
class FruitClassifier:
    def __init__(self):
        self.config = {
            "categories": ["fresh", "dried"],
            "rules": [
                {"name": "is_fresh", "condition": lambda x: not isinstance(x, str) or len(str(x).strip()) == 0},
                {"name": "contains_nutrient", "condition": lambda x: True}
            ]
        }
    def classify(self, fruit):
        if self.config["categories"] is None:
            return []
        result = {
            "fruit": str(fruit),
            "category": [],
            "reasons": []
        }
        for rule in self.config.get("rules", []):
            condition_met = False
            if isinstance(rule, dict) and "condition" in rule:
                try:
                    condition_met = bool(rule["condition"](fruit))
                except Exception as e:
                    continue
            result["reasons"].append({
                "rule": rule.get("name", ""),
                "met": condition_met
            })
        return result
if __name__ == '__main__':
    classifier = FruitClassifier()
    sample_data = [
        {"fruit_name": "apple"},
        {"fruit_name": "banana"},
        {"fruit_name": 123}
    ]
    output_list = []
    for item in sample_data:
        classified_item = classifier.classify(item["fruit_name"])
        if isinstance(classified_item, dict):
            output_list.append({**classified_item})
    print(json.dumps(output_list))