def convert_meters_to_yards(meters_list):
    yards_per_meter = 1.09361
    return [m * yards_per_meter for m in meters_list]

if __name__ == '__main__':
    sample_lengths = [1, 10, 100, 1000]
    result = convert_meters_to_yards(sample_lengths)
    print(result)