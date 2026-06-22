def convert_feet_to_inches(feet: float) -> float:
    return feet * 12.0

if __name__ == '__main__':
    feet_value: float = 5.5
    inches_value: float = convert_feet_to_inches(feet_value)
    print(inches_value)