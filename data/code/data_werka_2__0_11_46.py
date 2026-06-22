def convert_kilometers_to_miles(kilometers):
    conversion_factors = {'kilometers': 5}
    return kilometers * conversion_factors['kilometers']

if __name__ == '__main__':
    sample_distance = 20
    miles = convert_kilometers_to_miles(sample_distance)
    print(miles)