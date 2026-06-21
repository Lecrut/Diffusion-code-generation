def even_number_generator():
    for i in range(2, 101, 2):
        yield i

if __name__ == '__main__':
    generator = even_number_generator()
    sample_values = [next(generator) for _ in range(5)]
    print(sample_values)