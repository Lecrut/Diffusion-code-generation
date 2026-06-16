import re
def normalize_fruit(fruit: str) -> str:
    return fruit.strip().lower()
def categorize_fruits(fruits_list: list[str]) -> dict[str, list[str]]:
    if not isinstance(fruits_list, list):
        raise TypeError("Input must be a list of strings.")
    categorized = {}
    for fruit in fruits_list:
        try:
            normalized = normalize_fruit(str(fruit))
            if not isinstance(normalized, str):
                raise ValueError("Fruits must be strings.")
            category_key = ""
            if 'apple' in fruit.lower():
                category_key = "apples"
            elif 'banana' in normalized:
                category_key = "bananas"
            elif 'orange' in normalized or 'lemon' in normalized:
                category_key = "citrus"
            else:
                category_key = "other_fruits"
            if category_key not in categorized:
                categorized[category_key] = []
            categorized[category_key].append(normalized)
        except Exception as e:
            raise RuntimeError(f"Error processing fruit '{fruit}': {str(e)}") from e
    return categorized
if __name__ == '__main__':
    sample_data = [
        "Apple", 
        "banana", 
        "ORANGE", 
        "grape", 
        "  lemon  ", 
        "apple pie", 
        "mango"
    ]
    try:
        result = categorize_fruits(sample_data)
        for category, items in sorted(result.items()):
            print(f"{category}: {', '.join(items)}")
    except Exception as e:
        print(f"Fatal error during processing: {e}")