def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    sample_values = [4, 7, 10, 15, 22]
    results = {num: is_even(num) for num in sample_values}
    print(results)