def convert_kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    distance_in_meters = convert_kilometers_to_meters(5)
    print(distance_in_meters)