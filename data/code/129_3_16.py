class StringSorter:
    @staticmethod
    def sort_strings(strings):
        return sorted(strings, key=lambda s: (-len(s), s))

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    sorter = StringSorter()
    sorted_list = sorter.sort_strings(sample_list)
    print(sorted_list)