def generate_even_numbers(start, count):
    if start % 2 != 0:
        raise ValueError("Start value must be even.")
    if not isinstance(count, int) or count < 1:
        raise ValueError("Count must be a positive integer.")
    
    return list(range(start, start + count * 2, 2))

if __name__ == '__main__':
    try:
        start_value = 2
        number_of_evens = 10
        result = generate_even_numbers(start_value, number_of_evens)
        print(result)
    except ValueError as e:
        print(e)