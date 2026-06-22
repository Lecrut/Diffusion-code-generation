def compare_fathoms_meters(fathoms, meters):
    fathom_to_meter = 2.1336
    total_meters = fathoms * fathom_to_meter
    
    if total_meters > meters:
        return f"{fathoms} fathoms"
    elif total_meters < meters:
        return f"{meters} meters"
    else:
        return "Equal"

if __name__ == '__main__':
    print(compare_fathoms_meters(5, 12))