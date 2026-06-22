class WordReverser:
    def __init__(self, word):
        if not isinstance(word, str):
            raise ValueError("Input must be a string")
        self.word = word

    def reverse(self):
        reversed_word = ""
        for char in self.word:
            reversed_word = char + reversed_word
        return reversed_word

if __name__ == '__main__':
    sample_values = ["hello", "", "a", "Alibaba Cloud"]
    reverser_instances = [WordReverser(value) for value in sample_values]
    for instance in reverser_instances:
        print(instance.reverse())