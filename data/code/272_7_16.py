import random

class WordSorter:
    @staticmethod
    def generate_random_words(count):
        return [random.choice('abcdefghijklmnopqrstuvwxyz') * 3 for _ in range(count)]
    
    @classmethod
    def sort_alphabetically(cls, words):
        return sorted(words)

if __name__ == '__main__':
    sample1 = WordSorter.generate_random_words(4)
    result1 = WordSorter.sort_alphabetically(sample1)
    print(f"Sample 1 Input: {sample1}")
    print(f"Sample 1 Output: {result1}")

    sample2 = WordSorter.generate_random_words(4)
    result2 = WordSorter.sort_alphabetically(sample2)
    print(f"Sample 2 Input: {sample2}")
    print(f"Sample 2 Output: {result2}")

    sample3 = WordSorter.generate_random_words(4)
    result3 = WordSorter.sort_alphabetically(sample3)
    print(f"Sample 3 Input: {sample3}")
    print(f"Sample 3 Output: {result3}")

    sample4 = WordSorter.generate_random_words(5)
    result4 = WordSorter.sort_alphabetically(sample4)
    print(f"Sample 4 Input: {sample4}")
    print(f"Sample 4 Output: {result4}")