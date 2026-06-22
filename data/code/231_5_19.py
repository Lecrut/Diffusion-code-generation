def generate_pattern():
    pattern = 'A B C'
    for char in pattern:
        yield char

def limit_generator(generator, max_values):
    count = 0
    while count < max_values:
        try:
            value = next(generator)
            print(value, end=' ')
            count += 1
        except StopIteration:
            break

if __name__ == '__main__':
    pattern_gen = generate_pattern()
    limit_generator(pattern_gen, 30)