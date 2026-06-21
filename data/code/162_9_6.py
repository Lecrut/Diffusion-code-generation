country_iso_codes = frozenset({
    ('United States', 'US'),
    ('Canada', 'CA'),
    ('Mexico', 'MX'),
    ('Brazil', 'BR'),
    ('Argentina', 'AR')
})

if __name__ == '__main__':
    print(country_iso_codes)
    print(country_iso_codes.get('United States'))
    print(country_iso_codes.get('Germany', 'Unknown'))