from collections import Counter

class CharacterFrequencyComparer:
    def __init__(self, str1, str2):
        self.counter1 = Counter(str1)
        self.counter2 = Counter(str2)

    def get_difference(self):
        diff_counter = self.counter1 - self.counter2
        return dict(diff_counter)

if __name__ == '__main__':
    comparer = CharacterFrequencyComparer("hello", "world")
    result = comparer.get_difference()
    print(result)