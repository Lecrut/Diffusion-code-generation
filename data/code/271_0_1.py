import string
def categorize_string(input_string):
    categories = {
        "alphabetic": 0,
        "numeric": 0,
        "punctuation": 0,
        "whitespace": 0,
        "special_symbols": 0
    }
    for char in input_string:
        if char.isalpha():
            categories["alphabetic"] += 1
        elif char.isdigit():
            categories["numeric"] += 1
        elif char in string.punctuation:
            categories["punctuation"] += 1
        elif char.isspace():
            categories["whitespace"] += 1
        else:
            categories["special_symbols"] += 1
    return categories
if __name__ == '__main__':
    sample_string = "Hello World! 123$%^"
    results = categorize_string(sample_string)
    print(results)