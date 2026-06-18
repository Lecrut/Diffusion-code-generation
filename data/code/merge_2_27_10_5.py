from typing import Dict, List
def categorize_fruits(fruits: List[str]) -> Dict[str, List[str]]:
    categories = {
        'apples': [],
        'bananas': [],
        'citrus': []
    }
    fruits_lower = [f.lower() for f in fruits]
    for fruit in fruits_lower:
        matched_categories = []
        if any(fruit.startswith(cat) or cat in fruit 
               for cat in ['apples', 'apple']):
            categories['apples'].append(fruits[fruits_lower.index(fruit)])
        elif any(fruit.startswith(cat) or cat in fruit 
                 for cat in ['bananas', 'banana', 'plantain']):
            categories['bananas'].append(fruits[fruits_lower.index(fruit)])
        elif any(cat.lower() in fruit for cat in ['citrus', 'orange', 'lemon', 'lime']):
            categories['citrus'].append(fruits[fruits_lower.index(fruit)])
    return categories
if __name__ == '__main__':
    sample_fruits = [
        "Apple", 
        "Banana", 
        "Orange", 
        "Lemon", 
        "grapefruit",                                                                                                                                                    
        "peach",                                                                                                                 
    ]
    refined_samples = [
        "apple", "Apple", "APPLES", 
        "banana", "Banana", "BANANAS", 
        "orange", "Lemon", "Citrus"                                                                                                                                     
    ]
    test_data = [
        "red apples", "green Apple", "applesauce",
        "yellow bananas", "Banana bread", 
        "sour Citrus", "citrus fruits"
    ]
    result = categorize_fruits(test_data)
    for cat, items in result.items():
        print(f"{cat}: {items}")