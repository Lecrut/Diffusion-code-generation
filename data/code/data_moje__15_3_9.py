def fetch_second_last_int(values):
    if not hasattr(values, '__len__'):
        raise TypeError("Input must support length calculation")
    count = len(values)
    if count < 2:
        raise IndexError("List must contain at least two integers")
    return values[count - 2]

if __name__ == '__main__':
    sample_sequence = [100, 200, 300, 400, 500]
    outcome = fetch_second_last_int(sample_sequence)
    print(outcome)
    small_sequence = [99]
    try:
        fetch_second_last_int(small_sequence)
    except IndexError as err:
        print(err)