def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 10, 11]
    for val in sample_values:
        result = is_even(val)
        print(result)