from collections import Counter

def count_element_occurrences(data_list):
    return dict(Counter(data_list))

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 3, 3]
    occurrences = count_element_occurrences(sample_list)
    print(f"Occurrences of each element in {sample_list}: {occurrences}")