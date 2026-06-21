class WordAssigner:
    WORDS = ["one", "two", "three", "four", "five"]

    @staticmethod
    def initialize_dictionary(start, end):
        result = {}
        for i in range(start, end + 1):
            if i <= len(WordAssigner.WORDS):
                result[i] = WordAssigner.WORDS[i - 1]
            else:
                result[i] = f"word_{i}"
        return result

if __name__ == '__main__':
    sample_dict = WordAssigner.initialize_dictionary(1, 10)
    print(sample_dict)