class Sorter:
    def sort_list(self, data):
        return sorted(data)

if __name__ == '__main__':
    sorter = Sorter()
    numbers = [5, 2, 8, 1, 9, 3]
    sorted_numbers = sorter.sort_list(numbers)
    print(sorted_numbers)