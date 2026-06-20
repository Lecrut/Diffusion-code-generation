class StringSorter:
    def sort_strings(self, strings):
        sorted_strings = sorted(strings, key=lambda s: (-len(s), s))
        return sorted_strings

if __name__ == '__main__':
    string_list = [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry"
    ]
    sorter = StringSorter()
    sorted_list = sorter.sort_strings(string_list)
    print(sorted_list)