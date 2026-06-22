def compare_meters(meter1, meter2):
    if not isinstance(meter1, (int, float)) or not isinstance(meter2, (int, float)):
        raise ValueError('Both inputs must be numbers.')
    if meter1 > meter2:
        return meter1
    elif meter2 > meter1:
        return meter2
    else:
        return None
if __name__ == '__main__':
    longer_meters = compare_meters(3.5, 2.8)
    print(longer_meters)
    longer_meters = compare_meters(1.2, 1.2)
    print(longer_meters)