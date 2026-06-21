from collections import Counter

class ElementCounter:
    def __init__(self, list1, list2):
        self.counter1 = Counter(list1)
        self.counter2 = Counter(list2)

    def count_common(self):
        common_elements = self.counter1 & self.counter2
        return sum(common_elements.values())

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 5]
    sample_list2 = [4, 5, 5, 6, 7]
    counter_instance = ElementCounter(sample_list1, sample_list2)
    print(counter_instance.count_common())