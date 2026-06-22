def kilometers_to_meters(kilometers):
    conversion_factors = {'kilometers_to_meters': 1000}
    return kilometers * conversion_factors['kilometers_to_meters']
if __name__ == '__main__':
    sample_distances = [0.5, 1, 10, 100.75, -5]
    for distance in sample_distances:
        print(kilometers_to_meters(distance))