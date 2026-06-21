iso_codes = frozenset({('United States', 'US'), ('Canada', 'CA'), ('Mexico', 'MX')})

def get_iso_code(country):
    return next((code for name, code in iso_codes if name == country), None)
if __name__ == '__main__':
    print(get_iso_code('United States'))
    print(get_iso_code('Canada'))
    print(get_iso_code('Mexico'))
    print(get_iso_code('Germany'))