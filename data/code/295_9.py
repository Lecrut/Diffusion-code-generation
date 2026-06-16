def kg_to_lbs(kg):
    return kg * 2.20462
def lbs_to_kg(lbs):
    return lbs / 2.20462
if __name__ == '__main__':
    kilograms = 10
    pounds = 22.0462
    converted_pounds = kg_to_lbs(kilograms)
    print(f"{kilograms} kg is equal to {converted_pounds:.4f} lbs")
    converted_kg = lbs_to_kg(pounds)
    print(f"{pounds} lbs is equal to {converted_kg:.4f} kg")