def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

if __name__ == '__main__':
    sample_kg = [1, 5, 10, 20]
    sample_pounds = [2.20462, 11.0231, 22.0462, 44.0924]

    print("Kilograms to Pounds:")
    for kg in sample_kg:
        print(f"{kg} kg = {kg_to_pounds(kg):.2f} lbs")

    print("\nPounds to Kilograms:")
    for pounds in sample_pounds:
        print(f"{pounds} lbs = {pounds_to_kg(pounds):.2f} kg")