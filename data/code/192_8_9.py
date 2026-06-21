from collections import Counter

def count_common_elements(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    common_elements = set(counter1.keys()) & set(counter2.keys())
    total_count = sum((min(counter1[element], counter2[element]) for element in common_elements))
    return total_count
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 5]
    sample_list2 = [4, 5, 6, 7, 5, 5]
    print(count_common_elements(sample_list1, sample_list2))