from collections import Counter

def count_elements(data):
    return Counter(data)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = count_elements(sample_list)
    print(result)