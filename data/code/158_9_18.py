class NumberOperations:
    ODD_NUMBERS = {1, 3, 5, 7, 9, 11, 13, 15}

    @staticmethod
    def find_even_numbers(odd_set):
        all_numbers = set(range(1, 16))
        even_numbers = all_numbers - odd_set
        return even_numbers

if __name__ == '__main__':
    even_numbers = NumberOperations.find_even_numbers(NumberOperations.ODD_NUMBERS)
    print(even_numbers)