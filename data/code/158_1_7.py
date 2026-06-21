def get_even_numbers(start, end):
    return list(range(start, end + 1))[::2]

if __name__ == '__main__':
    start_value = 5
    end_value = 20
    even_numbers = get_even_numbers(start_value, end_value)
    print(even_numbers)