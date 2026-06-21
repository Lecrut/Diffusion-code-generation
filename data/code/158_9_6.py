class NumberProcessor:
    ODD_NUMBERS = {1, 3, 5, 7, 9, 11, 13, 15}
    
    @staticmethod
    def find_even_numbers():
        all_numbers = set(range(1, 16))
        even_numbers = all_numbers - NumberProcessor.ODD_NUMBERS
        return even_numbers

if __name__ == '__main__':
    print(NumberProcessor.find_even_numbers())