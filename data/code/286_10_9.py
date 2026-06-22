def inches_to_cm(inches):
    return inches * 2.54

if __name__ == '__main__':
    sample_inches = [1, 10, 100]
    for inches in sample_inches:
        print(f"{inches} inches is equal to {inches_to_cm(inches):.2f} cm")