sample_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
odd_numbers = tuple(filter(lambda x: x % 2 != 0, sample_data))
if __name__ == '__main__':
    print(odd_numbers)