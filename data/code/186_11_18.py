class StringSorter:
    DESCENDING = True

    @staticmethod
    def sort_strings(strings):
        return sorted(strings, reverse=StringSorter.DESCENDING)

if __name__ == '__main__':
    sample_values = ["banana", "apple", "cherry"]
    sorter = StringSorter()
    print(sorter.sort_strings(sample_values))