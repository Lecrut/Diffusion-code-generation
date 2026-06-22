def convert_kilometers_to_meters(distance_in_kilometers):
    meters_per_kilometer = 1000
    return distance_in_kilometers * meters_per_kilometer

if __name__ == '__main__':
    km = 12
    m = convert_kilometers_to_meters(km)
    print(m)