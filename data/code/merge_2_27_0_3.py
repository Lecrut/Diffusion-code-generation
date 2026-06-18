import re
def normalize_fruit(fruit: str) -> str:
    if not isinstance(fruit, str):
        raise TypeError("Input must be a string.")
    fruit = fruit.strip().lower()
    pattern = r'^([a-z]+)$'
    match = re.match(pattern, fruit)
    return ' '.join(match.groups())
def categorize_fruits(items: list[str]) -> dict[str, set]:
    categories = {}
    for item in items:
        try:
            normalized_item = normalize_fruit(item)
            if not normalized_item or len(normalized_item) > 20:
                raise ValueError(f"Invalid fruit name: '{item}'")
            category_key = f"{normalized_item[0]}{len(normalized_item)}"
            categories.setdefault(category_key, set()).add(normalized_item)
        except Exception as e:
            print(f"Error processing item {e}")
    return categories
if __name__ == '__main__':
    sample_data = [
        "Apple",
        "banana",
        "APPLE",
        "grape",
        123,
        None,
        "",
        "Cherry"
    ]
    result = categorize_fruits(sample_data)
    for category in sorted(result.keys()):
        print(f"{category}: {result[category]}")