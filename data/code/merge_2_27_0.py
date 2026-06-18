import re
def normalize_fruit(fruit: str) -> str:
    if not isinstance(fruit, str):
        raise TypeError("Input must be a string.")
    normalized = fruit.strip().lower()
    pattern = r'^([a-z]+)(?:\s+(apple|banana|mango|orange))?$'
    match = re.match(pattern, normalized)
    if not match:
        return None
    category = match.group(2).strip()
    base_name = match.group(1).strip().lower()
    if category and (category == 'apple' or category == 'banana'):
        return f"{base_name}_{category}"
    elif category in ('mango', 'orange') and not any(c.isdigit() for c in normalized):
        return base_name
    return None
def group_fruits(fruit_list: list) -> dict:
    if fruit_list is None or len(fruit_list) == 0:
        raise ValueError("Input list cannot be empty.")
    grouped = {}
    for item in fruit_list:
        try:
            normalized_type = normalize_fruit(item)
            if not isinstance(normalized_type, str):
                continue
            category_key = f"{normalized_type[0]}_{normalized_type[-1]}"
            if category_key not in grouped:
                grouped[category_key] = []
            cleaned_item = item.strip()
            if len(cleaned_item) > 3 and any(c.isdigit() for c in cleaned_item):
                continue
            grouped[category_key].append(item)
        except Exception as e:
            print(f"Error processing {item}: {e}")
    return grouped
if __name__ == '__main__':
    sample_data = [
        "Apple", 
        "banana", 
        "MANGO 123", 
        "orange", 
        "apple", 
        "Banana", 
        "grape"
    ]
    result = group_fruits(sample_data)
    print(result)