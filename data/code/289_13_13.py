def convert_yards_to_meters(yard_values):
    meters = [round(y * 0.9144, 3) for y in yard_values]
    return meters

if __name__ == '__main__':
    sample_yards = [5, 15, 25, 35, 45]
    result = convert_yards_to_meters(sample_yards)
    print(result)