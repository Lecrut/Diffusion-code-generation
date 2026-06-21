if __name__ == '__main__':
    sample_sequence = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    odd_numbers = tuple(num for num in sample_sequence if num % 2 != 0)
    print(odd_numbers)