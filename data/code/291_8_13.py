def compare_fathoms_meters(fathoms1, meters1, fathoms2, meters2):
    conversion_factor = 6
    length1 = fathoms1 * conversion_factor + meters1
    length2 = fathoms2 * conversion_factor + meters2
    if length1 == length2:
        return None
    elif length1 > length2:
        return (fathoms1, meters1, 'Fathoms')
    else:
        return (fathoms2, meters2, 'Meters')
if __name__ == '__main__':
    result = compare_fathoms_meters(5, 3, 4, 9)
    print(result)