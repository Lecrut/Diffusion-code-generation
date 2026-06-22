import random

class WordSorter:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def sort_words(self):
        return sorted(list(self.words))

if __name__ == '__main__':
    sorter = WordSorter()
    sorter.add_word("banana")
    sorter.add_word("apple")
    sorter.add_word("cherry")
    sorter.add_word("date")
    print(f"Sample 1 Input: ['banana', 'apple', 'cherry', 'date']")
    print(f"Sample 1 Output: {sorter.sort_words()}")

    sorter = WordSorter()
    sorter.add_word("zebra")
    sorter.add_word("ant")
    sorter.add_word("bear")
    sorter.add_word("cat")
    print(f"Sample 2 Input: ['zebra', 'ant', 'bear', 'cat']")
    print(f"Sample 2 Output: {sorter.sort_words()}")

    sorter = WordSorter()
    sorter.add_word("hello")
    sorter.add_word("world")
    sorter.add_word("python")
    sorter.add_word("java")
    print(f"Sample 3 Input: ['hello', 'world', 'python', 'java']")
    print(f"Sample 3 Output: {sorter.sort_words()}")

    sorter = WordSorter()
    sorter.add_word("a")
    sorter.add_word("b")
    sorter.add_word("c")
    sorter.add_word("d")
    sorter.add_word("e")
    print(f"Sample 4 Input: ['a', 'b', 'c', 'd', 'e']")
    print(f"Sample 4 Output: {sorter.sort_words()}")