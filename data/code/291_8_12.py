def validate_measurements(fathoms1, meters2):
    if not isinstance(fathoms1, (int, float)) or not isinstance(meters2, (int, float)):
        raise ValueError("Both measurements must be numbers.")
    return fathoms1, meters2

def convert_fathoms_to_meters(fathoms):
    return fathoms * 6.0

def compare_measurements(fathoms1, meters2):
    fathoms1, meters2 = validate_measurements(fathoms1, meters2)
    meters1 = convert_fathoms_to_meters(fathoms1)
    
    if meters1 > meters2:
        return (fathoms1, 'fathoms')
    elif meters1 < meters2:
        return (meters2, 'meters')
    else:
        return (meters1, 'meters')

if __name__ == '__main__':
    fathoms_a = 5
    meters_b = 30
    result = compare_measurements(fathoms_a, meters_b)
    print(f"The longer measure is {result[0]} {result[1]}")