country_codes = frozenset({('United States', 'US'), ('Canada', 'CA'), ('Mexico', 'MX'), ('Brazil', 'BR'), ('Argentina', 'AR')})

class CountryCodeMapper:
    def __init__(self, codes):
        self.codes = codes

    def get_iso_code(self, country_name):
        return next((code for name, code in self.codes if name == country_name), None)

if __name__ == '__main__':
    mapper = CountryCodeMapper(country_codes)
    print(mapper.get_iso_code('United States'))
    print(mapper.get_iso_code('Canada'))
    print(mapper.get_iso_code('Mexico'))
    print(mapper.get_iso_code('Brazil'))
    print(mapper.get_iso_code('Argentina'))
    print(mapper.get_iso_code('Germany'))