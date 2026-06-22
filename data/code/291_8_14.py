def compare_measures(fathoms, meters):
    fathom_to_meter = 20.25
    total_meters = fathoms * fathom_to_meter + meters
    if total_meters > fathoms:
        return f"{total_meters} meters"
    else:
        return f"{fathoms} fathoms"

if __name__ == '__main__':
    print(compare_measures(5, 100))