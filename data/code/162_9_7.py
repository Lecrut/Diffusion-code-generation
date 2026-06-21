country_codes = frozenset({
    ('United States', 'US'),
    ('Canada', 'CA'),
    ('Mexico', 'MX'),
    ('Brazil', 'BR'),
    ('Argentina', 'AR')
})

if __name__ == '__main__':
    print(country_codes)
    print(country_codes.get('United States'))