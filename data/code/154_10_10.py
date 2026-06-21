from collections import Counter

class ElementCounter:
    @staticmethod
    def count_elements(lst):
        return dict(Counter(lst))

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 3, 3]
    counter = ElementCounter()
    result = counter.count_elements(sample_list)
    print(result)