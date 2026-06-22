def contains_zero(iterable):
    for number in iterable:
        if number == 0:
            return True
    return False

if __name__ == '__main__':
    sample_values = [7, 8, 9, 0, 11]
    result = contains_zero(sample_values)
    print(result)