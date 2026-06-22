def nautical_miles_to_kilometers(nautical_miles):
    if nautical_miles == 0:
        return 0
    conversion_factor = 1.852
    kilometers = nautical_miles * conversion_factor
    return kilometers

if __name__ == '__main__':
    sample_distances = [0, 2, 20, 200]
    for distance in sample_distances:
        print(f"{distance} nautical miles is {nautical_miles_to_kilometers(distance)} kilometers")