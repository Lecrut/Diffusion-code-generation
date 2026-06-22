def yards_to_meters(yards):
    return [round(y * 0.9144, 3) for y in yards]

if __name__ == '__main__':
    sample_yards = [10, 20, 30]
    print(yards_to_meters(sample_yards))