class StringSorter:
    def sort_mixed_data(self, data):
        return sorted(data, key=lambda item: str(item))

if __name__ == '__main__':
    sorter = StringSorter()
    mixed_data = [5, "apple", 3, "banana"]
    sorted_data = sorter.sort_mixed_data(mixed_data)
    print(sorted_data)