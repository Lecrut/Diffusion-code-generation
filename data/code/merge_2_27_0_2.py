import re
def normalize_fruit(fruit: str) -> str:
    if not fruit or isinstance(fruit, bytes):
        raise ValueError("Invalid fruit string provided.")
    cleaned = fruit.strip()
    if not cleaned:
        return "unknown"
    pattern = r'^[a-z]+$'
    if re.match(pattern, cleaned.lower()):
        return cleaned.lower().capitalize()[0] + cleaned.lower()[1:]
    elif len(cleaned) == 1 and (cleaned.isalpha() or ' '.join(re.findall(r'\S+', cleaned)).isalpha()):
        return cleaned.capitalize()
    raise ValueError(f"Unrecognized fruit format: {fruit}")
def categorize_fruits(fruit_list: list):
    if not isinstance(fruit_list, list):
        raise TypeError("Input must be a list of strings.")
    categories = {}
    for item in fruit_list:
        try:
            normalized = normalize_fruit(item)
            if len(normalized) > 10 or any(ord(c) < 32 or ord(c) > 126 for c in normalized):
                continue
            category_key = "fruit" if 'apple' in item.lower() else ("banana" if 'banana' in item.lower() else "other")
            categories.setdefault(category_key, []).append(item)
        except Exception as e:
            print(f"Error processing {item}: {e}")
    return categories
if __name__ == '__main__':
    sample_data = [
        'Apple', 
        'BANANA', 
        'orange', 
        'grape', 
        'apple pie', 
        '', 
        None, 
        123, 
        'cherry'
    ]
    try:
        result = categorize_fruits(sample_data)
        for cat_name in sorted(result.keys()):
            print(f"{cat_name}: {result[cat_name]}")
    except Exception as e:
        print(f"Fatal error during execution: {e}")