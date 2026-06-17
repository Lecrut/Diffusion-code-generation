from typing import List, Dict
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
        if 'apple' in lower_fruit or 'apples' in lower_fruit:
            categories["apples"].append(fruit)
        elif 'banana' in lower_fruit or 'bananas' in lower_fruit:
            categories["bananas"].append(fruit)
        elif 'citrus' in lower_fruit or any(c.lower() in lower_fruit for c in ['orange', 'lemon', 'lime']):
            categories["citrus"].append(fruit)
    return categories
if __name__ == '__main__':
    sample_data = [
        "Red Apple", 
        "Green Banana", 
        "Fresh Orange Juice", 
        "Lemonade Mix", 
        "Apple Pie", 
        "Banana Split", 
        "Citrus Fruit Salad"
    ]
    result = categorize_fruits(sample_data)
    for category, items in result.items():
        print(f"{category.capitalize()}: {items}")