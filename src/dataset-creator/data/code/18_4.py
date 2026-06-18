def categorize_fruits(fruit_list):
    categorized = {}
    fruit_types = {
        "Apple": "Pome",
        "Banana": "Berry",
        "Orange": "Citrus",
        "Lemon": "Citrus",
        "Grape": "Berry",
        "Strawberry": "Berry",
        "Pineapple": "Tropical",
        "Mango": "Tropical"
    }
    for fruit in fruit_list:
        fruit_lower = fruit.lower()
        found_type = None
        for key, value in fruit_types.items():
            if key.lower() in fruit_lower or fruit_lower in key.lower():
                found_type = value
                break
        if found_type:
            if found_type not in categorized:
                categorized[found_type] = []
            categorized[found_type].append(fruit)
        else:
            if fruit not in categorized:
                categorized[fruit] = [fruit]
    return categorized
if __name__ == '__main__':
    sample_fruits = ["Apple", "Orange", "Banana", "Lemon", "Grape", "Pineapple", "Mango", "Pear"]
    result = categorize_fruits(sample_fruits)
    print(result)