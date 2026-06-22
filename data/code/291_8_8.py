def compare_measures(fathoms, meters):
    fathom_to_meter = 20.25
    meters_fathoms = meters / fathom_to_meter
    if meters_fathoms > fathoms:
        return f"{meters} meters"
    else:
        return f"{fathoms} fathoms"

if __name__ == '__main__':
    print(compare_measures(10, 205))