def compare_lengths(inches: float, centimeters: float) -> str:
    CM_PER_INCH = 2.54
    length_in_cm = inches * CM_PER_INCH
    if length_in_cm > centimeters:
        return f"{inches} inches is greater than {centimeters} centimeters"
    elif length_in_cm < centimeters:
        return f"{inches} inches is less than {centimeters} centimeters"
    else:
        return f"{inches} inches is equal to {centimeters} centimeters"

if __name__ == '__main__':
    sample_inches = 10
    sample_cm = 25
    print(compare_lengths(sample_inches, sample_cm))