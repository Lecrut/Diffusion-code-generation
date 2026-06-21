MAX_VALUE = 50

def generate_even_numbers(max_value):
    return [x for x in range(1, max_value + 1) if x % 2 == 0]

if __name__ == '__main__':
    even_numbers = generate_even_numbers(MAX_VALUE)
    print(even_numbers)