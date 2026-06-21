class NumberAnalyzer:
    @staticmethod
    def find_highest_number(numbers):
        highest = numbers[0]
        for num in numbers:
            if num > highest:
                highest = num
        return highest

if __name__ == '__main__':
    sample_numbers = [23, 67, 45, 89, 12]
    print(NumberAnalyzer.find_highest_number(sample_numbers))