import re
def normalize_fruit(fruit: str) -> str:
    return fruit.strip().lower()
def categorize_fruits(fruits_list: list[str]) -> dict[str, list[str]]:
    categories = {}
    for item in fruits_list:
        if not isinstance(item, str):
            raise TypeError("All items in the input list must be strings.")
        normalized_item = normalize_fruit(item)
        match_pattern = re.match(r'^([a-z]+)', normalized_item)
        if not match_pattern:
            continue
        base_category = match_pattern.group(1).capitalize()
        if base_category in categories:
            categories[base_category].append(normalized_item)
        else:
            categories[base_category] = [normalized_item]
    return categories
if __name__ == '__main__':
    sample_data = ['Apple', 'banana', 'cherry', 'APPLE', 'date', 'elderberry']
    result = categorize_fruits(sample_data)
    print(result)