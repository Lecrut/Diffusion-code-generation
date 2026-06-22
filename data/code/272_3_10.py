class WordSorter:
    def sort_words(self, input_string):
        words = input_string.split()
        sorted_words = sorted(words)
        return ' '.join(sorted_words)

if __name__ == '__main__':
    sorter = WordSorter()
    sample_input = "zebra apple mango banana cherry"
    result = sorter.sort_words(sample_input)
    print(result)