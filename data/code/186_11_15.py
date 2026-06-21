class StringSorter:
    @staticmethod
    def sort_desc(strings):
        return sorted(strings, reverse=True)

if __name__ == '__main__':
    sample_values = ["banana", "apple", "cherry"]
    sorter = StringSorter()
    print(sorter.sort_desc(sample_values))