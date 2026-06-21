class NumberFinder:
    @staticmethod
    def find_highest_number(numbers):
        highest = None
        for num in numbers:
            if highest is None or num > highest:
                highest = num
        return highest

if __name__ == '__main__':
    sample_numbers = [10, 65, 23, 89, 4]
    print(NumberFinder.find_highest_number(sample_numbers))