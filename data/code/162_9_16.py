COUNTRY_CODES = frozenset({('United States', 'US'), ('Canada', 'CA'), ('Mexico', 'MX')})

def get_iso_code(country_name):
    return next((code for name, code in COUNTRY_CODES if name == country_name), None)
if __name__ == '__main__':
    print(get_iso_code('United States'))
    print(get_iso_code('Canada'))
    print(get_iso_code('Mexico'))
    print(get_iso_code('Germany'))