class MaxFinder:
    @staticmethod
    def find_largest(numbers):
        if not numbers:
            raise ValueError("The tuple is empty")
        largest = numbers[0]
        for number in numbers[1:]:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    sample_tuple = (99, 45, 67, 12, 88)
    result = MaxFinder.find_largest(sample_tuple)
    print(result)