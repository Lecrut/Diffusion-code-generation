def get_even_numbers(start, end):
    numbers = list(range(start, end + 1))
    even_numbers = numbers[::2]
    return even_numbers

if __name__ == '__main__':
    start_val = 5
    end_val = 15
    result = get_even_numbers(start_val, end_val)
    print(result)