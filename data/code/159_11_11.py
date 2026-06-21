def odd_integers_generator(sample_values):
    for value in sample_values:
        if value % 2 != 0:
            yield value

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    generator = odd_integers_generator(sample_values)
    for value in generator:
        print(value)