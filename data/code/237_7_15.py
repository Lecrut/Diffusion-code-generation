def generate_even_numbers(count):
    return [2 * i for i in range(1, count + 1)]

if __name__ == '__main__':
    sample_count = 10
    result = generate_even_numbers(sample_count)
    print(result)