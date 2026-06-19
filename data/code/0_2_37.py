def inches_to_centimeters(inches):
    return inches * 2.54

if __name__ == '__main__':
    sample_inch_values = [1, 5, 10, 20]
    for inch in sample_inch_values:
        print(f"{inch} inches is {inches_to_centimeters(inch)} centimeters")