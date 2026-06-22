def miles_to_feet(miles):
    return miles * 5280.0

if __name__ == '__main__':
    sample_distances = [1.0, 0.5, 10.0, 2.5, 0.125]
    for distance in sample_distances:
        result = miles_to_feet(distance)
        print(result)