COUNTRY_CODES = frozenset((('United States', 'US'), ('Canada', 'CA'), ('Mexico', 'MX'), ('Brazil', 'BR'), ('Argentina', 'AR')))

def get_iso_code(country_name):
    for name, code in COUNTRY_CODES:
        if name == country_name:
            return code
    return None

if __name__ == '__main__':
    print(get_iso_code('United States'))
    print(get_iso_code('Canada'))
    print(get_iso_code('Mexico'))
    print(get_iso_code('Brazil'))
    print(get_iso_code('Argentina'))
    print(get_iso_code('Germany'))