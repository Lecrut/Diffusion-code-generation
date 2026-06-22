def compare_measures(fathoms, meters):
    fathom_to_meter = 20.25
    converted_meters = fathoms * fathom_to_meter

    if converted_meters > meters:
        return f"{fathoms} fathoms"
    elif converted_meters < meters:
        return f"{meters} meters"
    else:
        return "Equal measures"

if __name__ == '__main__':
    print(compare_measures(5, 100))