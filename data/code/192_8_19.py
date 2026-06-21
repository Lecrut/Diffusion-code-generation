from collections import Counter

def count_common_elements(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    common_elements = counter1 & counter2
    return sum(common_elements.values())

if __name__ == '__main__':
    sample_list1 = [1, 2, 2, 3, 4]
    sample_list2 = [2, 2, 3, 5]
    print(count_common_elements(sample_list1, sample_list2))