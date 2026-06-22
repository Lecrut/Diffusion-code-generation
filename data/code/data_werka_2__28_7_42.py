def is_larger(a, b):
    return a > b

if __name__ == '__main__':
    SAMPLE_VALUES = [(10, 5), (3, 7), (-1, -2), (0, 0)]
    for a, b in SAMPLE_VALUES:
        print(is_larger(a, b))