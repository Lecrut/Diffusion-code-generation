def compare_fathoms_meters(fathoms, meters):
    fathom_to_meter = 2
    if fathoms * fathom_to_meter > meters:
        return f"{fathoms} fathoms"
    else:
        return f"{meters} meters"

if __name__ == '__main__':
    print(compare_fathoms_meters(5, 10))