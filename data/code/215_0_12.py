class NumberIdentifier:
    @staticmethod
    def find_largest_number(numbers):
        return max(numbers)

if __name__ == '__main__':
    sample_data = [10, 5, 20, 3, 15]
    largest_number = NumberIdentifier.find_largest_number(sample_data)
    print(largest_number)