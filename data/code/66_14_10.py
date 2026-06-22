def convert_kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    distance_km = 5
    result = convert_kilometers_to_meters(distance_km)
    print(result)