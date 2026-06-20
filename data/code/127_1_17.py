def is_number_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    samples = [-1, 0, 1, 2, -3, 4, 5]
    for sample in samples:
        print(f"{sample}: {is_number_odd(sample)}")