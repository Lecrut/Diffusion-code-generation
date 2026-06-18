import json
class FruitGrouper:
    def __init__(self):
        self.config = {
            "categories": ["fresh", "dried"],
            "rules": [
                {"type": "category", "action": "add"},
                {"type": "weight_threshold", "value": 10, "unit": "g"}
            ]
        }
    def group(self, items):
        grouped = {}
        for item in items:
            category = self._determine_category(item)
            if category not in grouped:
                grouped[category] = []
            grouped[category].append(item)
        return grouped
    def _determine_category(self, fruit):
        rules = self.config["rules"]
        for rule in rules:
            if rule["type"] == "weight_threshold":
                weight = float(fruit.get("weight", 0))
                threshold = rule["value"] * (1 if rule["unit"] == "g" else 100)
                return f"dried" if weight > threshold else f"{fruit['name']}_fresh"
        return fruit["category"]
if __name__ == '__main__':
    fruits_data = [
        {"name": "apple", "weight": 5, "category": "fresh"},
        {"name": "banana", "weight": 120, "category": "dried"},
        {"name": "orange", "weight": 8, "category": "fresh"}
    ]
    grouper = FruitGrouper()
    result = grouper.group(fruits_data)
    output_config = {
        "config_file_path": "./fruit_classifier.json"
    }
    with open(output_config["config_file_path"], 'w') as f:
        json.dump(result, f, indent=4)