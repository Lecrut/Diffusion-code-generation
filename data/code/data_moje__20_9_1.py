def is_even(n):
    return not (n & 1)

if __name__ == '__main__':
    samples = {
        'even1': 2,
        'odd1': 3,
        'even2': 10,
        'odd2': 7,
        'zero': 0,
        'negative': -4
    }
    for name, value in samples.items():
        print(f'{name}: {is_even(value)}')