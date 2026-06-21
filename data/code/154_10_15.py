from collections import Counter

def count_elements(lst):
    return dict(Counter(lst))

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    result = count_elements(sample_list)
    print(f"Element counts: {result}")