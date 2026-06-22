def validate_input(meter1, meter2):
    if not isinstance(meter1, (int, float)) or not isinstance(meter2, (int, float)):
        raise ValueError('Both inputs must be numbers.')

def compare_meters(meter1, meter2):
    validate_input(meter1, meter2)
    if meter1 > meter2:
        return meter1
    elif meter2 > meter1:
        return meter2
    else:
        return None
if __name__ == '__main__':
    longer = compare_meters(5.0, 3.0)
    print(longer)
    longer = compare_meters(2.5, 4.5)
    print(longer)
    longer = compare_meters(7.0, 7.0)
    print(longer)