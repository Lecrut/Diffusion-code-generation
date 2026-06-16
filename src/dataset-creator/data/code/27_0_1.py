import re
def normalize_fruit(fruit: str) -> str:
    if not isinstance(fruit, str):
        raise TypeError("Input must be a string.")
    normalized = fruit.strip().lower()
    pattern = r'^\s*(apple|banana|mango|orange|grape)\b'
    match = re.match(pattern, normalized)
    if not match:
        return None
    return match.group(1).capitalize()
def group_fruits(fruit_list: list[str]) -> dict[str, list[str]]:
    categories = {}
    for fruit in fruit_list:
        try:
            category = normalize_fruit(fruit)
            if not category or category is None:
                raise ValueError("Invalid fruit type detected.")
            if category not in categories:
                categories[category] = []
            categories[category].append(fruit.strip())
        except Exception as e:
            print(f"Error processing '{fruit}': {e}")
    return categories
if __name__ == '__main__':
    sample_data = [
        'Apple',
        'banana',
        'mango',
        'ORANGE',
        'grape',
        'apple',
        'Watermelon'                                                                                 
    ]
    try:
        grouped = group_fruits(sample_data)
        for category, items in sorted(grouped.items()):
            print(f"{category}: {items}")
    except Exception as e:
        print(f"Fatal error during processing: {e}")