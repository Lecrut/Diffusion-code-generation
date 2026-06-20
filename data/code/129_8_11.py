class StringSorter:
    def sort_mixed_data(self, data):
        return sorted(map(str, data))

if __name__ == '__main__':
    sorter = StringSorter()
    mixed_data = ['apple', 10, 'banana', 5, 'cherry', 3]
    sorted_data = sorter.sort_mixed_data(mixed_data)
    print(sorted_data)