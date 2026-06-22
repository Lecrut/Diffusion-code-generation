def feet_to_inches(feet: float) -> float:
    return float(feet) * 12.0

if __name__ == '__main__':
    input_feet: float = 7.375
    output_inches: float = feet_to_inches(input_feet)
    print(output_inches)