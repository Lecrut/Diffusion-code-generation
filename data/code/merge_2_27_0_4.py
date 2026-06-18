import re
def normalize_fruit(fruit: str) -> str:
    return fruit.strip().lower()
def categorize_fruits(fruits_list: list[str]) -> dict[str, list[str]]:
    categories = {}
    if not fruits_list:
        return categories
    for item in fruits_list:
        try:
            normalized_item = normalize_fruit(item)
            match = re.match(r'^(\w+)', normalized_item, re.IGNORECASE)
            if not match:
                raise ValueError(f"Invalid fruit format: {item}")
            category_type = match.group(1).lower()
            if category_type not in categories:
                categories[category_type] = []
            categories[category_type].append(item)
        except Exception as e:
            print(f"Error processing '{item}': {e}")
    return categories
if __name__ == '__main__':
    sample_data = [
        "Apple",
        "banana",
        "Red Apple Pie",
        "GRAPE",
        "orange juice",
        "mango",
        "apple cider"
    ]
    grouped_fruits = categorize_fruits(sample_data)
    for category, items in sorted(grouped_fruits.items()):
        print(f"{category}: {items}")