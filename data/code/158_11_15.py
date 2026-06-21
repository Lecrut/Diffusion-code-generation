def even_number_generator():
    for number in range(2, 101, 2):
        yield number
if __name__ == '__main__':
    even_gen = even_number_generator()
    sample_values = [next(even_gen) for _ in range(5)]
    print(sample_values)