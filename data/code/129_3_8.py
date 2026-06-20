class StringSorter:
    def sort_strings(self, strings):
        return sorted(strings, key=lambda s: (-len(s), s))

if __name__ == '__main__':
    sorter = StringSorter()
    sample_list = ["apple", "banana", "cherry", "date", "elderberry"]
    sorted_list = sorter.sort_strings(sample_list)
    print(sorted_list)