country_codes = frozenset({('United States', 'US'), ('Canada', 'CA'), ('Mexico', 'MX'), ('Brazil', 'BR'), ('Argentina', 'AR')})

def validate_country_name(country_name):
    if not isinstance(country_name, str) or not country_name:
        raise ValueError("Invalid country name")

def get_iso_code(country_name):
    validate_country_name(country_name)
    return next((code for name, code in country_codes if name == country_name), None)

if __name__ == '__main__':
    print(get_iso_code('United States'))
    print(get_iso_code('Canada'))
    print(get_iso_code('Mexico'))
    print(get_iso_code('Brazil'))
    print(get_iso_code('Argentina'))
    print(get_iso_code('Germany'))