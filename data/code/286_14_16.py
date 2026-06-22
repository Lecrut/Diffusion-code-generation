conversion_factors = {'yards': 0.9144}

def yards_to_meters(yards):
    return yards * conversion_factors['yards']

if __name__ == '__main__':
    sample_yards = [1.0, 5.0, 10.5, 100.0]
    meters = yards_to_meters(sample_yards)
    print(meters)