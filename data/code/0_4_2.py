import math
def inches_to_cm(inches):
    centimeters = inches * 2.54
    return centimeters
if __name__ == '__main__':
    sample_inches = 10
    result = inches_to_cm(sample_inches)
    print(result)