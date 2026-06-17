from typing import Dict, List
def categorize_fruits(fruit_list: List[str]) -> Dict[str, List[str]]:
    categories = {
        "apples": [],
        "bananas": [],
        "citrus": []
    }
    for fruit in fruit_list:
        if isinstance(fruit, str):
            lower_fruit = fruit.lower()
            if 'apple' in lower_fruit or 'apples' in lower_fruit:
                categories["apples"].append(fruit)
            elif 'banana' in lower_fruit:
                categories["bananas"].append(fruit)
            elif 'citrus' in lower_fruit or 'orange' in lower_fruit or 'lemon' in lower_fruit:
                categories["citrus"].append(fruit)
    return categories
if __name__ == '__main__':
    sample_data = [
        "Apple", 
        "banana", 
        "Orange", 
        "Lemon", 
        "grapefruit", 
        "apple pie", 
        "Banana Split", 
        "Mango"                                                                                    
    ]
    result = categorize_fruits(sample_data)
    for cat_name, items in result.items():
        print(f"{cat_name.capitalize()}: {items}")