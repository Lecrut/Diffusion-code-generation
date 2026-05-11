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
        if "apple" in lower_item or "banana" in lower_item or "orange" in lower_item:
            categories["fruit"].append(item)
        elif "carrot" in lower_item or "broccoli" in lower_item or "spinach" in lower_item:
            categories["vegetable"].append(item)
        elif "beef" in lower_item or "pork" in lower_item or "chicken" in lower_item:
            categories["meat"].append(item)
        elif "milk" in lower_item or "cheese" in lower_item:
            categories["dairy"].append(item)
        else:
            categories["other"].append(item)
    return categories
if __name__ == '__main__':
    sample_data = [
        "Apple is a fruit",
        "Carrot is a vegetable",
        "Beef is meat",
        "Banana is a fruit",
        "Broccoli is a vegetable",
        "Milk is dairy",
        "Steak is meat",
        "Book is not food"
    ]
    result = categorize_strings(sample_data)
    print(result)