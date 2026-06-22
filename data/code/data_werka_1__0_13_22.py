def kilometers_to_miles(kilometers):
    miles_per_kilometer = 5
    return kilometers * miles_per_kilometer

if __name__ == '__main__':
    sample_kilometers = 10
    result = kilometers_to_miles(sample_kilometers)
    print(result)