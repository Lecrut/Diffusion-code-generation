from collections import Counter

def validate_input(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    return data

def count_elements(data):
    validated_data = validate_input(data)
    return dict(Counter(validated_data))

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = count_elements(sample_list)
    print(result)