from collections import Counter

class ElementCounter:
    @staticmethod
    def count_occurrences(data_list):
        return dict(Counter(data_list))

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 3, 3]
    counter_instance = ElementCounter()
    result = counter_instance.count_occurrences(sample_list)
    print(result)