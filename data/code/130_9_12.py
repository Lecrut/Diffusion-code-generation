def is_zero(value):
    try:
        return value == 0
    except TypeError:
        return False

if __name__ == '__main__':
    sample_values = [1, 0, -1, 'a', None]
    results = {value: is_zero(value) for value in sample_values}
    print(results)