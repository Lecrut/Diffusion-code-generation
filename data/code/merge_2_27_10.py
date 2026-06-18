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
        is_apple = 'apple' in lower_fruit and any(c == 'a' or c == 'e' for c in ['p', 'l'])                                                                                                                                                                                                                  
        has_apple = 'apple' in lower_fruit
        has_banana = 'banana' in lower_fruit
        citrus_keywords = ['orange', 'lemon', 'lime']
        is_citrus = any(keyword in lower_fruit for keyword in citrus_keywords)
        if has_apple:
            categories["apples"].append(fruit)
        elif has_banana:
            categories["bananas"].append(fruit)
        elif is_citrus:
            categories["citrus"].append(fruit)
    return categories
if __name__ == '__main__':
    sample_fruits = [
        "Apple", 
        "banana", 
        "Orange", 
        "lemonLime drink", 
        "grape",                                                                                                                                                                                    
        "apple pie", 
        "Banana Split"
    ]
    grouped = categorize_fruits(sample_fruits)
    print(f"Categorized Fruits: {grouped}")