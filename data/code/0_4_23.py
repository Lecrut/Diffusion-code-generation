def convert_meters_to_yards(meters):
    return meters * 1.09361

if __name__ == '__main__':
    lengths_in_meters = [1, 10, 100]
    for length in lengths_in_meters:
        yards = convert_meters_to_yards(length)
        print(yards)