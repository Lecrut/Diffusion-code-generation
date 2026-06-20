def compare_lengths_gen(len_a, len_b):
    yield len_a > len_b
    yield len_a < len_b
    yield len_a == len_b

if __name__ == '__main__':
    for result in compare_lengths_gen(10, 10):
        print(result)