def compare_measures(nanometers, micrometers):
    nanometers_to_micrometers = nanometers / 1000
    if nanometers_to_micrometers < micrometers:
        return f"{nanometers} nm"
    else:
        return f"{micrometers} µm"

if __name__ == '__main__':
    print(compare_measures(500, 0.4))