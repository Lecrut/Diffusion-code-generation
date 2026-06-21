from collections import Counter

def count_elements(lst):
    return Counter(lst)

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 3, 3]
    print(count_elements(sample_list))