class NumberUtils:
    ODD_NUMBERS = {1, 3, 5, 7, 9, 11, 13, 15}

    @staticmethod
    def find_even_numbers(odd_set):
        all_numbers = set(range(1, 16))
        return all_numbers - odd_set

if __name__ == '__main__':
    even_numbers = NumberUtils.find_even_numbers(NumberUtils.ODD_NUMBERS)
    print(even_numbers)