def is_odd(number):
    return number & 1 == 1

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, 5, -1, -2, -3]
    results = {num: is_odd(num) for num in sample_values}
    print(results)