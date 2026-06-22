def generate_even_numbers(start=2, count=10):
    even_numbers = []
    for num in range(start, start + count * 2, 2):
        even_numbers.append(num)
    return even_numbers

if __name__ == '__main__':
    sample_result = generate_even_numbers()
    print(sample_result)