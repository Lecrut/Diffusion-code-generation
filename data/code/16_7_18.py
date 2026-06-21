def get_leading_element(sequence):
    try:
        return next(iter(sequence))
    except StopIteration:
        raise IndexError("Cannot get leading element from empty sequence")

if __name__ == '__main__':
    sample_data = [7, 14, 21, 28]
    output = get_leading_element(sample_data)
    print(output)