from collections import Counter

def count_common_elements(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    common_elements = counter1 & counter2
    return sum(common_elements.values())

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50, 50]
    sample_list2 = [40, 50, 50, 60, 70]
    common_count = count_common_elements(sample_list1, sample_list2)
    print(common_count)