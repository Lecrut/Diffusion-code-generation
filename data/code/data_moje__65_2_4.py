CONVERSION_FACTOR = 12

def feet_to_inches(feet):
    if feet < 0:
        raise ValueError("Feet cannot be negative")
    if feet == 0:
        return 0
    return feet * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_values = [0, 3, 10.5, -1]
    for value in sample_values:
        try:
            output = feet_to_inches(value)
            print(f"{value} feet is {output} inches")
        except ValueError as e:
            print(f"Error for {value} feet: {e}")