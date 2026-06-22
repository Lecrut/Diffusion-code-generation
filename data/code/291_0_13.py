def compare_meters(meter1: float, meter2: float) -> float:
    if meter1 > meter2:
        return meter1
    elif meter2 > meter1:
        return meter2
    else:
        raise ValueError("Meters are equal")

if __name__ == '__main__':
    length_a = 5.7
    length_b = 3.2
    longer_length = compare_meters(length_a, length_b)
    print(f"The longer length is: {longer_length} meters")