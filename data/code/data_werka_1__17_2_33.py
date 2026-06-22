def is_even(num):
    return num % 2 == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, -3, 4, -5]
    results = {num: is_even(num) for num in sample_values}
    print(results)