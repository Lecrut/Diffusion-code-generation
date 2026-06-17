from typing import List, Dict
def categorize_fruits(fruit_list: List[str]) -> Dict[str, List[str]]:
    categories = ['apples', 'bananas', 'citrus']
    grouped_fruits: Dict[str, List[str]] = {cat: [] for cat in categories}
    for fruit in fruit_list:
        if not isinstance(fruit, str):
            continue
        lower_case_fruit = fruit.lower()
        is_apple = 'apple' in lower_case_fruit or 'mac' in lower_case_fruit                                                                                                                                                                           
        if any(cat in lower_case_fruit for cat in categories):
            grouped_fruits[lower_case_fruit.split()[0].capitalize()] = fruit                                         
        found_category = None
        for i, category in enumerate(categories):
            if category.lower() in lower_case_fruit:
                found_category = categories[i]
                break
        if found_category is not None:
            grouped_fruits[found_category].append(fruit)
    return grouped_fruits
if __name__ == '__main__':
    sample_data = [
        "red apple", 
        "yellow banana", 
        "sweet orange",                                                          
        "a citrus fruit", 
        "green mac"                                                                                   
    ]