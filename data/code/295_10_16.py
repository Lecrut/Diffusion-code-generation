def validate_km(km):
    if not isinstance(km, (int, float)):
        raise ValueError("Kilometers must be a numeric value.")
    return km

def convert_km_to_miles(km):
    return validate_km(km) * 0.621371

if __name__ == '__main__':
    metric_length = 10.0
    print(convert_km_to_miles(metric_length))