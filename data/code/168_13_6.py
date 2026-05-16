def categorize_strings(string_list):
    categories = {
        "fruit": [],
        "vegetable": [],
        "meat": [],
        "dairy": [],
        "other": []
    }
    fruit_keywords = ['apple', 'banana', 'orange', 'grape', 'strawberry']
    vegetable_keywords = ['carrot', 'broccoli', 'spinach', 'potato', 'tomato']
    meat_keywords = ['beef', 'pork', 'chicken', 'fish']
    dairy_keywords = ['milk', 'cheese', 'yogurt']
    for item in string_list:
        item_lower = item.lower()
        if any(keyword in item_lower for keyword in fruit_keywords):
            categories["fruit"].append(item)
        elif any(keyword in item_lower for keyword in vegetable_keywords):
            categories["vegetable"].append(item)
        elif any(keyword in item_lower for keyword in meat_keywords):
            categories["meat"].append(item)
        elif any(keyword in item_lower for keyword in dairy_keywords):
            categories["dairy"].append(item)
        else:
            categories["other"].append(item)
    return categories
if __name__ == '__main__':
    sample_data = [
        "Apple is a fruit",
        "Carrot is a vegetable",
        "Beef is meat",
        "Milk is dairy",
        "Banana is a fruit",
        "Broccoli is a vegetable",
        "Chicken is meat",
        "Cheese is dairy",
        "Book is a general item"
    ]
    result = categorize_strings(sample_data)
    print(result)