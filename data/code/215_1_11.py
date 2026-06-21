class MaxFinder:
    def find_largest(self, numbers):
        largest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    finder = MaxFinder()
    sample_tuple = (99, 45, 67, 12, 88)
    result = finder.find_largest(sample_tuple)
    print(result)