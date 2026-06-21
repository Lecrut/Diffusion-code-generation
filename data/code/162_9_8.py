country_codes = frozenset({('United States', 'US'), ('Canada', 'CA'), ('Mexico', 'MX'), ('Brazil', 'BR'), ('Argentina', 'AR')})

class CountryCodeLookup:
    def __init__(self, codes):
        self._codes = codes

    def get_iso_code(self, country_name):
        return next((code for name, code in self._codes if name == country_name), None)

if __name__ == '__main__':
    lookup = CountryCodeLookup(country_codes)
    print(lookup.get_iso_code('United States'))
    print(lookup.get_iso_code('Canada'))
    print(lookup.get_iso_code('Mexico'))
    print(lookup.get_iso_code('Brazil'))
    print(lookup.get_iso_code('Argentina'))
    print(lookup.get_iso_code('Germany'))