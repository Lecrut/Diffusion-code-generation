def check_even(number):
    if number < 0:
        return not (number % 2)
    else:
        return not (number % 2)

if __name__ == '__main__':
    results = []
    for val in [10, 15, 22, -3, 0]:
        results.append(check_even(val))
    print(results)