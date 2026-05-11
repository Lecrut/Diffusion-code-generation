def categorize_strings(string_list):
    categories = {
        "fruit": [],
        "vegetable": [],
        "meat": [],
        "dairy": [],
        "other": []
    }
    for item in string_list:
        lower_item = item.lower()
        if any(keyword in lower_item for keyword in ["apple", "banana", "orange", "grape", "strawberry"]):
            categories["fruit"].append(item)
        elif any(keyword in lower_item for keyword in ["carrot", "broccoli", "spinach", "potato", "tomato"]):
            categories["vegetable"].append(item)
        elif any(keyword in lower_item for keyword in ["beef", "pork", "chicken", "lamb"]):
            categories["meat"].append(item)
        elif any(keyword in lower_item for keyword in ["milk", "cheese", "yogurt"]):
            categories["dairy"].append(item)
        else:
            categories["other"].append(item)
    return categories
if __name__ == '__main__':
    sample_data = [
        "apple",
        "carrot",
        "beef",
        "banana",
        "broccoli",
        "milk",
        "spinach",
        "chicken",
        "grape",
        "water"
    ]
    result = categorize_strings(sample_data)
    print(result)