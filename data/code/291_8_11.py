def compare_fathoms_and_meters(fathoms1, meters2):
    fathoms_to_meters = fathoms1 * 6
    if fathoms_to_meters > meters2:
        return (fathoms1, 'fathoms')
    elif fathoms_to_meters < meters2:
        return (meters2, 'meters')
    else:
        return (fathoms1, 'fathoms')

if __name__ == '__main__':
    result1 = compare_fathoms_and_meters(5, 30)
    print(f'Comparison of 5 fathoms and 30 meters: {result1}')
    result2 = compare_fathoms_and_meters(4, 23)
    print(f'Comparison of 4 fathoms and 23 meters: {result2}')