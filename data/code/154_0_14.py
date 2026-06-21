from collections import Counter

def count_occurrences(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    
    return Counter(data)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = count_occurrences(sample_list)
    print(result)