def compare_measures(nanometers, micrometers):
    if nanometers < micrometers * 1000:
        return f"{nanometers} nm"
    return f"{micrometers} um"

if __name__ == '__main__':
    print(compare_measures(500, 2))