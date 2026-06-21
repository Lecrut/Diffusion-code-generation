if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    
    def is_odd(number):
        return number % 2 != 0
    
    odd_numbers = tuple(filter(is_odd, sample_tuple))
    print(odd_numbers)