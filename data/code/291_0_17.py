def compare_meters(meter1: float, meter2: float) -> float:
    if meter1 > meter2:
        return meter1
    else:
        return meter2

if __name__ == '__main__':
    longer_length = compare_meters(5.5, 7.0)
    print(f"The longer length is: {longer_length} meters")
    longer_length = compare_meters(3.0, 3.0)
    print(f"The longer length is: {longer_length} meters")