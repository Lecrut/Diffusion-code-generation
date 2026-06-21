def generate_even_numbers():
    for num in range(2, 101, 2):
        yield num

if __name__ == '__main__':
    even_gen = generate_even_numbers()
    sample_values = [next(even_gen) for _ in range(5)]
    print(sample_values)