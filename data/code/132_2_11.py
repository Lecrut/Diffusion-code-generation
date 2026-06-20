def check_condition(n):
    return n > 0 and not (n & 1)

if __name__ == '__main__':
    sample_values = [5, -3, 0, 2, 7]
    results = {value: check_condition(value) for value in sample_values}
    print(results)