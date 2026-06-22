YARDS_TO_KILOMETERS = 0.0009144

def yards_to_kilometers(yards):
    return yards * YARDS_TO_KILOMETERS
if __name__ == '__main__':
    sample_value = 1000.5
    result = yards_to_kilometers(sample_value)
    print(result)