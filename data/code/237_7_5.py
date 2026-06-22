def generate_even_numbers(start=2, count=10):
    sequence = []
    for _ in range(count):
        sequence.append(start)
        start += 2
    return sequence

if __name__ == '__main__':
    start_value = 4
    number_of_elements = 5
    result = generate_even_numbers(start=start_value, count=number_of_elements)
    print(result)