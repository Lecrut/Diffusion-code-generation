conversion_factor = 2.54

def inches_to_cm(inches):
    return inches * conversion_factor

if __name__ == '__main__':
    print(f"Conversion factor from inches to centimeters: {inches_to_cm(1)} cm")