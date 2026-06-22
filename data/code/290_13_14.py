def tons_to_kilograms(tons):
    kilograms = tons * 907.184
    return round(kilograms, 2)

if __name__ == '__main__':
    sample_tons = [3.5, 7.25, 0.5, 15.0]
    for tons in sample_tons:
        print(tons_to_kilograms(tons))