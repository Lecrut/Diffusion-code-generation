def calculate_absolute_difference(volume1, volume2):
    difference = abs(volume1 - volume2)
    return f"{difference:.2f}"

if __name__ == '__main__':
    sample_values = {
        'volume_a': 107.984,
        'volume_b': 103.567
    }
    
    result = calculate_absolute_difference(sample_values['volume_a'], sample_values['volume_b'])
    print(result)