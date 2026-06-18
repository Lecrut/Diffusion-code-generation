from typing import List, Dict
def categorize_fruits(fruit_list: List[str]) -> Dict[str, List[str]]:
    categories = ['apples', 'bananas', 'citrus']
    categorized_fruits: Dict[str, List[str]] = {cat: [] for cat in categories}
    priority_order = {'apples': 0, 'bananas': 1, 'citrus': 2}
    for fruit in fruit_list:
        if not isinstance(fruit, str):
            continue
        lower_fruit = fruit.lower()
        assigned_category = None
        for cat_idx, cat_name in enumerate(categories):
            if cat_name in lower_fruit:
                assigned_category = cat_name
                break
        if assigned_category is not None and fruit not in categorized_fruits[assigned_category]:
            categorized_fruits[assigned_category].append(fruit)
    return categorized_fruits
if __name__ == '__main__':
    sample_data = [
        "Red Delicious", 
        "Banana Split", 
        "Orange Juice", 
        "apple pie", 
        "grapefruit salad", 
        "banana bread", 
        "mango smoothie"                                                                                                                
    ]
    result = categorize_fruits(sample_data)
    print("Categorized Fruits:")
    for cat in ['apples', 'bananas', 'citrus']:
        if result[cat]:
            print(f"{cat.capitalize()}: {result[cat]}")