def compare_fathoms_and_meters(fathoms1, meters2):
    fathom_to_meter = 60
    if not isinstance(fathoms1, (int, float)) or not isinstance(meters2, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    
    fathoms_in_meters = fathoms1 * fathom_to_meter
    return (fathoms_in_meters, 'm') if fathoms_in_meters > meters2 else (meters2, 'm')

if __name__ == '__main__':
    print(compare_fathoms_and_meters(3, 200))
    print(compare_fathoms_and_meters(5.5, 331))