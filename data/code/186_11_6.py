class StringSorter:
    @staticmethod
    def sort_desc(words):
        return sorted(words, reverse=True)

if __name__ == '__main__':
    sample_words = ["apple", "zebra", "banana", "cat", "dog"]
    sorter = StringSorter()
    sorted_list = sorter.sort_desc(sample_words)
    print(sorted_list)