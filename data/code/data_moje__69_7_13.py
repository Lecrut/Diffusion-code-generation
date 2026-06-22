def miles_to_feet_generator(durations_in_miles):
    feet_per_mile = 5280
    for mile in durations_in_miles:
        yield mile * feet_per_mile

if __name__ == '__main__':
    sample_distances = (1, 3, 5, 10, 100)
    for feet_value in miles_to_feet_generator(sample_distances):
        print(feet_value)