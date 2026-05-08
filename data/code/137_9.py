def categorize_strings(string_list):
    result = []
    for s in string_list:
        if len(s) < 10:
            category = 'Short'
        elif len(s) < 50:
            category = 'Medium'
        else:
            category = 'Long'
        result.append(category)
    return result
if __name__ == '__main__':
    sample_strings = ["apple", "banana", "kiwi", "strawberry", "grapefruit", "watermelon", "blueberry", "raspberry", "orange", "pineapple", "this is a very long string"]
    categorized = categorize_strings(sample_strings)
    print(categorized)