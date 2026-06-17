def kg_to_lbs(kg):
    return kg * 2.20462
def lbs_to_kg(lbs):
    return lbs / 2.20462
if __name__ == '__main__':
    kilograms = 10
    pounds = 22.0462
    converted_pounds = kg_to_lbs(kilograms)
    print(f"{kilograms} kilograms is equal to {converted_pounds} pounds")
    converted_kilograms = lbs_to_kg(pounds)
    print(f"{pounds} pounds is equal to {converted_kilograms} kilograms")