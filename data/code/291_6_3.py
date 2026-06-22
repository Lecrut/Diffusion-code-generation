def compare_measures(nanometers, micrometers):
    if not isinstance(nanometers, (int, float)) or not isinstance(micrometers, (int, float)):
        raise ValueError("Both inputs must be numbers")
    
    if nanometers < micrometers * 1000:
        return f"{nanometers} nm"
    else:
        return f"{micrometers} um"

if __name__ == '__main__':
    print(compare_measures(500, 2))