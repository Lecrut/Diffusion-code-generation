def inches_to_cm(inches):
    centimeters = inches * 2.54
    return centimeters
if __name__ == '__main__':
    sample_inches = 10
    result = inches_to_cm(sample_inches)
    print(f"{sample_inches} inches is equal to {result} centimeters")
    sample_inches = 39.3701
    result = inches_to_cm(sample_inches)
    print(f"{sample_inches} inches is equal to {result} centimeters")