def convert_feet_to_inches(feet: float) -> float:
    return feet * 12.0

if __name__ == '__main__':
    result = convert_feet_to_inches(5.5)
    print(result)