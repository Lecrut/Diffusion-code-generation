def is_positive(number):
    try:
        num = int(number)
        return num > 0
    except ValueError:
        return False

if __name__ == '__main__':
    sample_values = [10, -5, 'abc', 0, 23]
    results = {value: is_positive(value) for value in sample_values}
    print(results)