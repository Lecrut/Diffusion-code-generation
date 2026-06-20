def is_even(number):
    return number & 1 == 0

if __name__ == '__main__':
    sample_numbers = [2, 3, 4, -6, -7]
    results = {num: is_even(num) for num in sample_numbers}
    print(results)