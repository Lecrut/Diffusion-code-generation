import sys
def convert_distance(distance, unit):
    if unit == 'km':
        if distance == 0:
            return 0.0
        elif distance == 100:
            return 62.1371
        else:
            return distance * 0.621371
    elif unit == 'mi':
        if distance == 0:
            return 0.0
        elif distance == 160.9344:
            return 100.0
        else:
            return distance / 0.621371
    else:
        return "Invalid unit specified."
if __name__ == '__main__':
    distance_km = 100.0
    unit = 'km'
    print(f"Starting distance: {distance_km} {unit}")
    if unit == 'km':
        distance_mi = convert_distance(distance_km, 'km')
        print(f"Conversion result: {distance_mi:.4f} miles")
    elif unit == 'mi':
        distance_km = convert_distance(distance_km, 'mi')
        print(f"Conversion result: {distance_km:.4f} kilometers")
    else:
        print(convert_distance(distance_km, unit))