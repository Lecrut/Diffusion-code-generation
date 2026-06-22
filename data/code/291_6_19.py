CONVERSION_FACTOR = 1000

def compare_measures(nanometers, micrometers):
    if nanometers < micrometers * CONVERSION_FACTOR:
        return f"{nanometers} nm"
    else:
        return f"{micrometers} um"

if __name__ == '__main__':
    print(compare_measures(500, 2))