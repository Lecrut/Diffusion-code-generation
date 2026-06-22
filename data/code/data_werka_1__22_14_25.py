def is_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, -1, -2, -3]
    results = {num: is_odd(num) for num in sample_values}
    print(results)