conversion_factor = {'pounds_to_kg': 0.453592}

def pounds_to_kilograms(pounds):
    return pounds * conversion_factor['pounds_to_kg']

if __name__ == '__main__':
    sample_pounds = 100.0
    result_kg = pounds_to_kilograms(sample_pounds)
    print(f"{sample_pounds} pounds is {result_kg} kilograms")