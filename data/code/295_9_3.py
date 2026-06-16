def kg_to_lbs(kg):
    return kg * 2.20462
def lbs_to_kg(lbs):
    return lbs / 2.20462
if __name__ == '__main__':
    kilograms = 10
    pounds = 22.0462
    print(f"{kilograms} kg is equal to {kg_to_lbs(kilograms)} lbs")
    print(f"{pounds} lbs is equal to {lbs_to_kg(pounds)} kg")