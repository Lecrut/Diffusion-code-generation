import re
def normalize_string(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    s = s.strip().lower()
    return s
def categorize_fruits(fruit_list: list) -> dict:
    categories = {}
    for fruit in fruit_list:
        try:
            normalized = normalize_string(str(fruit))
            if not normalized or len(normalized) > 20:
                continue
            match_type = re.match(r'^([a-z]+)', normalized, re.IGNORECASE)
            if not match_type:
                raise ValueError("Invalid fruit type detected.")
            category = match_type.group(1).capitalize()
            if category in categories:
                categories[category].append(fruit)
            else:
                categories[category] = [fruit]
        except Exception as e:
            print(f"Error processing '{fruit}': {e}")
    return categories
if __name__ == '__main__':
    sample_data = ['Apple', 'banana', 'GRAPE', 'orange', 123, None, '', 'Mango']
    grouped_fruits = categorize_fruits(sample_data)
    for category, items in sorted(grouped_fruits.items()):
        print(f"{category}: {items}")