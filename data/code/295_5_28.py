conversion_factor = 2.54

def inches_to_cm(inches):
    return inches * conversion_factor

if __name__ == '__main__':
    sample_inches = 8
    print(f"{sample_inches} inches is {inches_to_cm(sample_inches)} cm")