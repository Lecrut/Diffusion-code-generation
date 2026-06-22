METERS_TO_KILOMETERS = 1000

def compare_lengths(length1: float, length2: float) -> float:
    if length1 > length2:
        return length1
    else:
        return length2

if __name__ == '__main__':
    sample_length1 = 500.0
    sample_length2 = 750.0
    longer_length = compare_lengths(sample_length1, sample_length2)
    print(f"The longer length is {longer_length} meters.")