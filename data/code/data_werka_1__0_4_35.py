def convert_meters_to_yards(meters_list):
    yards_list = [m * 1.09361 for m in meters_list]
    return yards_list

if __name__ == '__main__':
    sample_lengths = [1, 10, 100, 1000]
    result = convert_meters_to_yards(sample_lengths)
    print(result)