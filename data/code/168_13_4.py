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
    for s in string_list:
        s_lower = s.lower()
        if any(keyword in s_lower for keyword in fruit_keywords):
            categories["fruit"].append(s)
        elif any(keyword in s_lower for keyword in vegetable_keywords):
            categories["vegetable"].append(s)
        elif any(keyword in s_lower for keyword in meat_keywords):
            categories["meat"].append(s)
        elif any(keyword in s_lower for keyword in dairy_keywords):
            categories["dairy"].append(s)
        else:
            categories["other"].append(s)
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
        "Water is not a food item",
        "Cheese is dairy"
    ]
    result = categorize_strings(sample_data)
    print(result)