class NumberFinder:
    @staticmethod
    def find_highest_number(numbers):
        highest = numbers[0]
        for num in numbers:
            if num > highest:
                highest = num
        return highest

if __name__ == '__main__':
    sample_numbers = [15, 23, 7, 90, 48]
    print(NumberFinder.find_highest_number(sample_numbers))