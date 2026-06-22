def tons_to_kilograms(tons):
    return round(tons * 907.184, 2)

if __name__ == '__main__':
    sample_tons = [1.5, 10.25, 500.75, 0.001]
    for tons in sample_tons:
        print(tons_to_kilograms(tons))