from collections import Counter

def count_element_occurrences(data_list):
    return dict(Counter(data_list))

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    element_counts = count_element_occurrences(sample_list)
    print(f"Element counts in {sample_list}: {element_counts}")