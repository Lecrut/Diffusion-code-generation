class StringSorter:
    @staticmethod
    def sort_by_length(strings):
        return sorted(strings, key=len)

if __name__ == '__main__':
    sample_values = ["blueberry", "strawberry", "raspberry", "blackberry", "gooseberry"]
    sorter = StringSorter()
    sorted_values = sorter.sort_by_length(sample_values)
    print(sorted_values)