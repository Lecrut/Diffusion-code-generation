def compare_meters(meter1, meter2):
    if meter1 > meter2:
        return meter1
    else:
        return meter2

if __name__ == '__main__':
    sample_meters_a = 5.0
    sample_meters_b = 7.5
    longer_meter = compare_meters(sample_meters_a, sample_meters_b)
    print(f"The longer length is: {longer_meter} meters")