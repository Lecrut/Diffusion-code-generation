def convert_kilometers_to_miles(kilometers):
    if kilometers < 0:
        raise ValueError("Distance cannot be negative")
    return kilometers * 5

if __name__ == '__main__':
    sample_kilometers = 20
    miles = convert_kilometers_to_miles(sample_kilometers)
    print(miles)