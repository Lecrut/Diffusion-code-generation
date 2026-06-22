class NumberSorter:
    @staticmethod
    def sort_numbers():
        numbers = [34, 7, 23]
        sorted_numbers = sorted(numbers)
        return sorted_numbers

if __name__ == '__main__':
    sorter = NumberSorter()
    result = sorter.sort_numbers()
    print(result)