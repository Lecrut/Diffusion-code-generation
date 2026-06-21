from collections import Counter

class StringCounter:
    @staticmethod
    def count_and_sort(strings):
        return dict(Counter(strings).most_common())

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = StringCounter.count_and_sort(sample_strings)
    print(result)