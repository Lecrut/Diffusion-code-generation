if __name__ == '__main__':
    start_range = 0
    end_range = 50
    even_numbers_list = [number for number in range(start_range, end_range + 1) if number % 2 == 0]
    print(even_numbers_list)