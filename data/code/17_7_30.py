def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = {num: is_even(num) for num in sample_values}
    print(results)