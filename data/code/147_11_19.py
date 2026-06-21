class StringSorter:
    def sort_alphabetically(self, input_list):
        return sorted(input_list, key=str.lower)

if __name__ == '__main__':
    sorter = StringSorter()
    sample_values = ["banana", "Apple", "cherry", "date"]
    print(sorter.sort_alphabetically(sample_values))