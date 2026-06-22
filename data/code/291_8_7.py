def compare_measures(fathoms, meters):
    fathom_to_meter = 20.25
    total_meters = fathoms * fathom_to_meter + meters
    if total_meters > meters:
        return f"{fathoms} fathoms"
    else:
        return f"{meters} meters"

if __name__ == '__main__':
    print(compare_measures(10, 205))