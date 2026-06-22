def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

if __name__ == '__main__':
    sample_kilometers = 10.0
    miles = kilometers_to_miles(sample_kilometers)
    print(miles)