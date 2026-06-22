conversion_factor = 1000

def tons_to_kg(tons):
    return int(tons * conversion_factor)

if __name__ == '__main__':
    mass_value = 5
    result_kg = tons_to_kg(mass_value)
    print(f"{mass_value} tons is {result_kg} kg")