CONVERSION_FACTOR = 907.184

def tons_to_kilograms(tons):
    return round(tons * CONVERSION_FACTOR, 2)

if __name__ == '__main__':
    sample_tons = [2.5, 3.75, 0.1, 10.0]
    for tons in sample_tons:
        print(tons_to_kilograms(tons))