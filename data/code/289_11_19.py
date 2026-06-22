def meters_to_feet(meters):
    return [round(m * 3.28084, 2) for m in meters]

if __name__ == '__main__':
    sample_meters = [1, 2, 3, 4, 5]
    print(meters_to_feet(sample_meters))