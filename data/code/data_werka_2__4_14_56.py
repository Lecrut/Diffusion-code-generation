def normalize_distance(value, unit):
    if unit == 'meters':
        return value
    elif unit == 'kilometers':
        return value * 1000
    elif unit == 'miles':
        return value * 1609.34
    else:
        raise ValueError("Unsupported unit")

if __name__ == '__main__':
    distances = [
        (5, 'meters'),
        (2, 'kilometers'),
        (1, 'miles')
    ]
    
    for distance, unit in distances:
        normalized_distance = normalize_distance(distance, unit)
        print(f"{distance} {unit} is {normalized_distance} meters")