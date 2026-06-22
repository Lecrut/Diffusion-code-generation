def compare_lengths(nanometers, micrometers):
    nanometers_to_micrometers = nanometers / 1000
    if nanometers_to_micrometers < micrometers:
        return f"{nanometers} nm"
    else:
        return f"{micrometers} um"

if __name__ == '__main__':
    print(compare_lengths(500, 0.6))