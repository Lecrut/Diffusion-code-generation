def categorize_fruits(fruit_list):
    categorized = {}
    fruit_types = {
        "Citrus": ["Orange", "Lemon", "Lime"],
        "Pome": ["Apple", "Pear"],
        "Berry": ["Strawberry", "Blueberry", "Raspberry"],
        "Melon": ["Watermelon", "Cantaloupe"]
    }
    for fruit in fruit_list:
        found = False
        for fruit_type, fruits in fruit_types.items():
            if fruit in fruits:
                if fruit_type not in categorized:
                    categorized[fruit_type] = []
                if fruit not in categorized[fruit_type]:
                    categorized[fruit_type].append(fruit)
                found = True
                break
        if not found:
            if fruit not in categorized:
                categorized[fruit] = [fruit]
    return categorized
if __name__ == '__main__':
    sample_fruits = [
        "Apple",
        "Orange",
        "Banana",
        "Lemon",
        "Strawberry",
        "Pear",
        "Watermelon",
        "Grape",
        "Lime"
    ]
    result = categorize_fruits(sample_fruits)
    print(result)