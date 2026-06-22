conversion_factor = {
    'tons_to_kilograms': 907.184
}

def tons_to_kilograms(tons):
    kilograms = tons * conversion_factor['tons_to_kilograms']
    return round(kilograms, 2)

if __name__ == '__main__':
    sample_tons = [2.5, 3.75, 0.1, 10.0]
    for tons in sample_tons:
        print(tons_to_kilograms(tons))