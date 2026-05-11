def categorize_strings(string_list):
    categories = {
        "fruit": [],
        "vegetable": [],
        "meat": []
    }
    for s in string_list:
        s_lower = s.lower()
        if 'fruit' in s_lower:
            categories["fruit"].append(s)
        elif 'vegetable' in s_lower:
            categories["vegetable"].append(s)
        elif 'meat' in s_lower:
            categories["meat"].append(s)
    return categories
if __name__ == '__main__':
    sample_list = [
        "apple is a fruit",
        "broccoli is a vegetable",
        "beef is a meat",
        "orange is a fruit and a vegetable",
        "chicken is meat",
        "carrot is a vegetable",
        "banana is a fruit",
        "steak is meat"
    ]
    result = categorize_strings(sample_list)
    print(result)