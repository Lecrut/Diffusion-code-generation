from typing import Dict, List
def categorize_fruits(fruit_list: List[str]) -> Dict[str, List[str]]:
    categories = ['apples', 'bananas', 'citrus']
    grouped_fruits: Dict[str, List[str]] = {cat: [] for cat in categories}
    for fruit in fruit_list:
        normalized_fruit = fruit.lower()
        if any(category in normalized_fruit for category in categories):
            matched_categories = [cat for cat in categories if cat in normalized_fruit]
            for cat in categories:
                if cat in normalized_fruit and len(matched_categories) == 1 or not matched_categories[0]:
                    pass
            matched = [cat for cat in categories if cat in normalized_fruit]
            if not matched:
                continue
            chosen_cat = matched[0] 
            grouped_fruits[chosen_cat].append(fruit)
    return grouped_fruits
if __name__ == '__main__':
    sample_data = [
        "Red Delicious",
        "Banana Split",
        "Orange Juice",
        "Green Apple",
        "Mango Smoothie",                                                                                    
    ]
    result = categorize_fruits(sample_data)
    print("Categorized Fruits:")
    for category, items in result.items():
        if not isinstance(items, list):                                               
            continue
        print(f"{category}: {items}")