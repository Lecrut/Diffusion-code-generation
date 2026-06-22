def compare_measures(nanometers, micrometers):
    if not isinstance(nanometers, (int, float)) or not isinstance(micrometers, (int, float)):
        raise ValueError("Both inputs must be numbers")
    conversion_factor = 1000
    if nanometers < micrometers * conversion_factor:
        return f"{nanometers} nm"
    else:
        return f"{micrometers} um"

if __name__ == '__main__':
    print(compare_measures(500, 2))