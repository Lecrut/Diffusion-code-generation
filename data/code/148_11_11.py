class MaxFinder:
    @staticmethod
    def find_largest(numbers):
        if not numbers:
            return None
        
        largest = numbers[0]
        for number in numbers[1:]:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    sample_data = [10, 5, 20, 15, 30]
    result = MaxFinder.find_largest(sample_data)
    print(result)