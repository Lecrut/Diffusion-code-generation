def convert_to_milliliters(volumes):
    conversion_factors = {
        'liters': 1000.0,
        'gallons': 3785.411784,
        'cubic_inches': 16.387064
    }
    
    results = []
    
    for volume, unit in volumes:
        if volume < 0:
            results.append(0.0)
        elif volume == 0:
            results.append(0.0)
        else:
            factor = conversion_factors.get(unit.lower())
            if factor is None:
                results.append(0.0)
            else:
                results.append(volume * factor)
    
    return results

if __name__ == '__main__':
    sample_volumes = [
        (1, 'liters'),
        (2.5, 'gallons'),
        (100, 'cubic_inches'),
        (0, 'liters'),
        (-5, 'gallons'),
        (0.5, 'liters')
    ]
    
    converted = convert_to_milliliters(sample_volumes)
    print(converted)