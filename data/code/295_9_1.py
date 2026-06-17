def kg_to_lbs(kilograms):
    return kilograms * 2.20462
def lbs_to_kg(pounds):
    return pounds / 2.20462
if __name__ == '__main__':
    weight_kg = 10
    weight_lbs = kg_to_lbs(weight_kg)
    print(f"{weight_kg} kilograms is equal to {weight_lbs} pounds")
    weight_lbs_sample = 150
    weight_kg_sample = lbs_to_kg(weight_lbs_sample)
    print(f"{weight_lbs_sample} pounds is equal to {weight_kg_sample} kilograms")