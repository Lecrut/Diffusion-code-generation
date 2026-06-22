def compare_measures(nanometers, micrometers):
    conversion_factor = 1000
    if nanometers < micrometers * conversion_factor:
        shorter_measure = nanometers
        unit = "nm"
    else:
        shorter_measure = micrometers
        unit = "um"
    return f"{shorter_measure} {unit}"

if __name__ == '__main__':
    result = compare_measures(300, 1)
    print(result)