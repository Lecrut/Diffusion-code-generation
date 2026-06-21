from collections import Counter

def validate_input(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    if not all(isinstance(item, (int, str)) for item in data):
        raise ValueError("List items must be integers or strings")

def count_elements(data):
    validate_input(data)
    return Counter(data)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = count_elements(sample_list)
    print(result)