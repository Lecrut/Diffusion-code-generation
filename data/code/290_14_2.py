def kg_to_lbs(kg):
    return round(kg * 2.20462, 2)

def lbs_to_kg(lbs):
    return round(lbs / 2.20462, 2)
if __name__ == '__main__':
    print(kg_to_lbs(1))
    print(kg_to_lbs(5))
    print(lbs_to_kg(2.2))
    print(lbs_to_kg(11.02))