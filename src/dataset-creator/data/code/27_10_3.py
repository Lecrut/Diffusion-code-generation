from typing import Dict, List
def categorize_fruits(fruit_list: List[str]) -> Dict[str, List[str]]:
    categories = {
        "apples": [],
        "bananas": [],
        "citrus": []
    }
    for fruit in fruit_list:
        if not isinstance(fruit, str):
            continue
        lower_fruit = fruit.lower()
        if 'apple' in lower_fruit or 'red apple' in lower_fruit:
            categories["apples"].append(fruit)
        elif 'banana' in lower_fruit:
            categories["bananas"].append(fruit)
        elif any(x in lower_fruit for x in ['orange', 'lemon', 'lime']):
            categories["citrus"].append(fruit)
    return categories
if __name__ == '__main__':
    sample_data = [
        "Red Apple", 
        "Green Banana Peel", 
        "Orange Juice", 
        "Lemonade", 
        "Apple Pie", 
        "Banana Bread", 
        "Mango Smoothie"                                                                  
    ]
    result = categorize_fruits(sample_data)
    print("Categorized Fruits:")
    for category, items in result.items():
        if items:
            print(f"{category.capitalize()}: {', '.join(items)}")