class WordSearcher:
    @staticmethod
    def contains_word(sequence, target):
        return any(word == target for word in sequence)

if __name__ == '__main__':
    sample_sequence = ["apple", "banana", "cherry"]
    target_word = "grape"
    print(WordSearcher.contains_word(sample_sequence, target_word))