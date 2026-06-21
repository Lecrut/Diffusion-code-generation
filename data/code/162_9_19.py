country_codes = frozenset({('United States', 'US'), ('Canada', 'CA'), ('Mexico', 'MX'), ('Brazil', 'BR'), ('Argentina', 'AR')})

def get_iso_code(country_name):
    return next((code for name, code in country_codes if name == country_name), None)

if __name__ == '__main__':
    sample_country = 'Canada'
    iso_code = get_iso_code(sample_country)
    print(f"The ISO code for {sample_country} is: {iso_code}")