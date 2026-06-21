class LargestNumberFinder:
    @staticmethod
    def find_largest(numbers):
        largest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    sample_data1 = [10, 5, 20, 8]
    result1 = LargestNumberFinder.find_largest(sample_data1)
    print(result1)

    sample_data2 = [-5, -1, -10, -3]
    result2 = LargestNumberFinder.find_largest(sample_data2)
    print(result2)

    sample_data3 = [42]
    result3 = LargestNumberFinder.find_largest(sample_data3)
    print(result3)

    sample_data4 = [7]
    result4 = LargestNumberFinder.find_largest(sample_data4)
    print(result4)