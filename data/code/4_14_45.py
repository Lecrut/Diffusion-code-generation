def normalize_distance(distance, unit):
    if unit == 'meters':
        return distance
    elif unit == 'kilometers':
        return distance * 1000
    elif unit == 'miles':
        return distance * 1609.34
    else:
        raise ValueError("Unsupported unit of measurement")

if __name__ == '__main__':
    distances = [
        (10, 'meters'),
        (5, 'kilometers'),
        (2, 'miles')
    ]

    for distance, unit in distances:
        normalized_distance = normalize_distance(distance, unit)
        print(f"{distance} {unit} is {normalized_distance} meters")