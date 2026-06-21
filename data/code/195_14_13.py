from collections import Counter

class WordCountComparer:
    @staticmethod
    def _lowercase_counter(words):
        return Counter(word.lower() for word in words)

    @staticmethod
    def compare(list1, list2):
        counter1 = WordCountComparer._lowercase_counter(list1)
        counter2 = WordCountComparer._lowercase_counter(list2)
        diff_counter = counter1 - counter2
        return dict(diff_counter)

if __name__ == '__main__':
    sample_list1 = ['Apple', 'banana', 'Cherry', 'apple']
    sample_list2 = ['Banana', 'cherry', 'date']
    result = WordCountComparer.compare(sample_list1, sample_list2)
    print(result)