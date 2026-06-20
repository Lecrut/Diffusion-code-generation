def convert_kilometers_to_miles(kilometers):
    return kilometers / 5.0

if __name__ == '__main__':
    kilometers_value = 100
    miles_value = convert_kilometers_to_miles(kilometers_value)
    print(miles_value)