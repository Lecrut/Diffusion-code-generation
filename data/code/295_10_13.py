conversion_factors = {
    'kilometers_to_miles': 0.621371,
}

def kilometers_to_miles(kilometers):
    return kilometers * conversion_factors['kilometers_to_miles']

if __name__ == '__main__':
    sample_km = 10.0
    print(kilometers_to_miles(sample_km))