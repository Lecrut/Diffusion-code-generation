class CountryCodeMapper:
    COUNTRY_CODES = frozenset({
        ('United States', 'US'),
        ('Canada', 'CA'),
        ('Mexico', 'MX'),
        ('Brazil', 'BR'),
        ('Argentina', 'AR')
    })

    @staticmethod
    def get_iso_code(country_name):
        return next((code for name, code in CountryCodeMapper.COUNTRY_CODES if name == country_name), None)

if __name__ == '__main__':
    mapper = CountryCodeMapper()
    print(mapper.get_iso_code('United States'))
    print(mapper.get_iso_code('Canada'))
    print(mapper.get_iso_code('Mexico'))
    print(mapper.get_iso_code('Brazil'))
    print(mapper.get_iso_code('Argentina'))
    print(mapper.get_iso_code('Germany'))