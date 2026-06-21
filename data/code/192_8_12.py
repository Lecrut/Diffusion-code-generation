from collections import Counter

class ElementCounter:
    def __init__(self, list1, list2):
        self.counter1 = Counter(list1)
        self.counter2 = Counter(list2)

    def count_common_elements(self):
        common_elements = self.counter1 & self.counter2
        return sum(common_elements.values())

if __name__ == '__main__':
    list_a_sample = [1, 2, 3, 4, 5, 5]
    list_b_sample = [4, 5, 5, 6, 7, 8]
    
    element_counter = ElementCounter(list_a_sample, list_b_sample)
    result = element_counter.count_common_elements()
    print(result)