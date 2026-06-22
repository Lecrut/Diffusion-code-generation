def yards_to_kilometers(yards):
    conversion_factor = 0.0254 * 39.3701 / 1000
    return yards * conversion_factor

if __name__ == '__main__':
    sample_yards = 100.5
    result = yards_to_kilometers(sample_yards)
    print(result)