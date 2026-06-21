from collections import Counter

def count_elements(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    return dict(Counter(lst))

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 3, 3]
    print(count_elements(sample_list))