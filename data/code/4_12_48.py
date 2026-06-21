METERS_TO_KILOMETERS = 1 / 1000
KILOMETERS_TO_METERS = 1000

def convert_distance(value, unit):
    if unit == 'm':
        return value * METERS_TO_KILOMETERS
    elif unit == 'km':
        return value * KILOMETERS_TO_METERS
    else:
        raise ValueError("Unsupported unit. Use 'm' for meters or 'km' for kilometers.")

if __name__ == '__main__':
    distance_in_meters = 1500
    distance_in_kilometers = convert_distance(distance_in_meters, 'm')
    print(f"{distance_in_meters} meters is {distance_in_kilometers} kilometers")
    
    distance_in_kilometers = 2.5
    distance_in_meters = convert_distance(distance_in_kilometers, 'km')
    print(f"{distance_in_kilometers} kilometers is {distance_in_meters} meters")