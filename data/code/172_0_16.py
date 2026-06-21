class DictionarySorter:
    def __init__(self):
        self.data = {
            "apple": "fruit",
            "zebra": "animal",
            "banana": "fruit",
            "cat": "animal",
            "dog": "animal"
        }

    def sort_values(self):
        words = list(self.data.values())
        words.sort()
        return words

if __name__ == '__main__':
    sorter = DictionarySorter()
    sorted_list = sorter.sort_values()
    print(sorted_list)