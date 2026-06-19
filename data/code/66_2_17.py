class ArrayComparator:
    def check_adjacencies(self, numbers):
        comparisons = []
        for index in range(len(numbers) - 1):
            first_number = numbers[index]
            second_number = numbers[index + 1]
            comparison_pair = (first_number, second_number)
            comparisons.append(comparison_pair)
        return comparisons

if __name__ == '__main__':
    comparator_instance = ArrayComparator()
    test_numbers = [4, 9, 1, 3, 7]
    adjacent_pairs = comparator_instance.check_adjacencies(test_numbers)
    print(adjacent_pairs)