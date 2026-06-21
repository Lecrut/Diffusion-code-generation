def generate_even_numbers(max_value):
    return [x for x in range(1, max_value + 1) if x % 2 == 0]

if __name__ == '__main__':
    max_value = 50
    even_numbers = generate_even_numbers(max_value)
    print(even_numbers)