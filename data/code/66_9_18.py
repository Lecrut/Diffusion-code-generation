DISTANCE_MULTIPLIER = 1000
def calculate_meters(distance_in_km):
    return distance_in_km * DISTANCE_MULTIPLIER
def transform_distances(kilometer_values):
    return tuple(map(calculate_meters, kilometer_values))
if __name__ == '__main__':
    initial_distances = (10, 20.5, 30, 45.75)
    final_meters = transform_distances(initial_distances)
    print(final_meters)