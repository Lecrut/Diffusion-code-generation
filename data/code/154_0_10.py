from collections import Counter

def count_elements(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    return Counter(data)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = count_elements(sample_list)
    print(result)