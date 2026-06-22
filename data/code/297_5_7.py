def inches_to_cm(inches):
    conversion_factor = 2.54
    return inches * conversion_factor

if __name__ == '__main__':
    sample_inches = 10
    result_cm = inches_to_cm(sample_inches)
    print(result_cm)