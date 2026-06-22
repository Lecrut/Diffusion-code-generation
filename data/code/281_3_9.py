def sum_of_six_numbers(a, b, c, d, e, f):
    return a + b + c + d + e + f

if __name__ == '__main__':
    numbers = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6
    }
    result = sum_of_six_numbers(**numbers)
    print(result)