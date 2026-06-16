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
            match_pattern = re.match(r'^([a-z]+)', normalized_item)
            if not match_pattern or len(match_pattern.group(1)) == 0:
                continue
            fruit_type = match_pattern.group(1).capitalize()
            if fruit_type in categories:
                categories[fruit_type].append(normalized_item)
            else:
                categories[fruit_type] = [normalized_item]
        except Exception as e:
            print(f"Error processing item '{item}': {e}")
    return categories
if __name__ == '__main__':
    sample_data = ['Apple', 'banana', 'GRAPE', 'apple pie', 'orange juice', 'Banana bread']
    result = categorize_fruits(sample_data)
    print(result)