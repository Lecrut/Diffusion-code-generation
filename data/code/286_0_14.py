INCHES_TO_CM = 2.54

def inches_to_cm(inches):
    return inches * INCHES_TO_CM

if __name__ == '__main__':
    sample_inches = [3, 12, 0, -5]
    results = [(inches, inches_to_cm(inches)) for inches in sample_inches]
    print(results)