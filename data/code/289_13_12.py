def yards_to_meters(yards):
    conversion_factor = 0.9144
    return [round(y * conversion_factor, 3) for y in yards]

if __name__ == '__main__':
    sample_yards = [5, 15, 25]
    print(yards_to_meters(sample_yards))