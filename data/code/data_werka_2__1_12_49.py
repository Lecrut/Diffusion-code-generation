def kg_to_pounds(kg):
    conversion_factor = 2.20462
    return kg * conversion_factor

def pounds_to_kg(pounds):
    conversion_factor = 2.20462
    return pounds / conversion_factor
if __name__ == '__main__':
    sample_kilograms = 90
    sample_pounds = 198
    pounds_result = kg_to_pounds(sample_kilograms)
    print(f'{sample_kilograms} kg is {pounds_result:.2f} pounds')
    kilograms_result = pounds_to_kg(sample_pounds)
    print(f'{sample_pounds} pounds is {kilograms_result:.2f} kg')