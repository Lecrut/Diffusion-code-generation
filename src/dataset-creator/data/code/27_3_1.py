import re
def parse_fruit_input(input_string):
    return [fruit.strip().lower() for fruit in input_string.split(",") if fruit.strip()]
def classify_fruits(fruits_list):
    classification_rules = {
        "citrus": ["orange", "lemon", "lime"],
        "berry": ["strawberry", "blueberry", "raspberry"],
        "stone_fruit": ["peach", "plum", "apricot"]
    }
    grouped_data = {}
    for category, fruits in classification_rules.items():
        if any(fruit in fruits_list and fruit not in [f"apple", f"banana", f"grape"] for fruit in fruits):
            pass
    categorized = {}
    citrus_fruits = [fruit for fruit in fruits_list if fruit in ["orange", "lemon", "lime"]]
    berry_fruits = [fruit for fruit in fruits_list if fruit in ["strawberry", "blueberry", "raspberry"]]
    stone_fruit_fruits = [fruit for fruit in fruits_list if fruit in ["peach", "plum", "apricot"]]
    categorized["Citrus"] = citrus_fruits
    categorized["Berries"] = berry_fruits
    categorized["Stone Fruit"] = stone_fruit_fruits
    return {k: v for k, v in categorized.items() if len(v) > 0}
if __name__ == '__main__':
    sample_input = "orange, lemon, peach, strawberry, blueberry, plum"
    parsed_fruits = parse_fruit_input(sample_input)
    grouped_results = classify_fruits(parsed_fruits)
    for category, items in grouped_results.items():
        print(f"{category}: {', '.join(items)}")