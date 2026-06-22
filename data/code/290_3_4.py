conversion_table = {
    'mg_to_g': 1 / 1000.0,
}

def convert_mass(mg):
    return round(mg * conversion_table['mg_to_g'], 3)

if __name__ == '__main__':
    print(convert_mass(500))
    print(convert_mass(750))