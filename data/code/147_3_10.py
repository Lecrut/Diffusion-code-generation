class FloatSorter:
    @staticmethod
    def sort_descending(numbers):
        return sorted(numbers, reverse=True)

if __name__ == '__main__':
    numbers = [3.5, 1.2, 4.8, 2.9]
    sorted_numbers = FloatSorter.sort_descending(numbers)
    print(sorted_numbers)