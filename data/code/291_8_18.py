FATHOM_TO_METERS = 6
METERS_TO_FATHOMS = 1 / FATHOM_TO_METERS

def compare_length(fathoms1, meters2):
    fathoms2_in_fathoms = meters2 * METERS_TO_FATHOMS
    if fathoms1 > fathoms2_in_fathoms:
        return (fathoms1, "fathoms")
    else:
        return (fathoms2_in_fathoms, "meters")

if __name__ == '__main__':
    length_a = 5
    length_b = 30
    result = compare_length(length_a, length_b)
    print(f"Longer measure: {result[0]} {result[1]}")