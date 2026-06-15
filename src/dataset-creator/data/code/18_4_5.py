def categorize_fruits(fruit_list):
    categorized = {}
    fruit_types = {
        "Apple": "Pome",
        "Orange": "Citrus",
        "Lemon": "Citrus",
        "Banana": "Berry",
        "Strawberry": "Berry",
        "Grape": "Berry",
        "Pineapple": "Tropical",
        "Mango": "Tropical",
        "Lime": "Citrus"
    }
    for fruit in fruit_list:
        found = False
        for key, fruit_type in fruit_types.items():
            if fruit in key:
                fruit_type_name = fruit_types[key]
                if fruit_type_name not in categorized:
                    categorized[fruit_type_name] = []
                categorized[fruit_type_name].append(fruit)
                found = True
                break
        if not found:
            if fruit not in categorized:
                categorized[fruit] = [fruit]
    return categorized
if __name__ == '__main__':
    sample_fruits = ["Apple", "Orange", "Lemon", "Banana", "Strawberry", "Grape", "Pineapple", "Mango", "Lime", "Watermelon"]
    result = categorize_fruits(sample_fruits)
    print(result)