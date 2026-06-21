def kg_to_pounds(kg):
    return kg * 2.20462262185

def pounds_to_kg(pounds):
    return pounds / 2.20462262185

if __name__ == '__main__':
    sample_kg = 70
    sample_pounds = 154

    converted_pounds = kg_to_pounds(sample_kg)
    converted_kg = pounds_to_kg(sample_pounds)

    print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")