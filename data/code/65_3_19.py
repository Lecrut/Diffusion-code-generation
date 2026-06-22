def feet_to_inches(feet: float) -> float:
    return feet * 12

if __name__ == '__main__':
    sample_feet_values = [1.0, 5.5, 10.0, 0.25]
    for value in sample_feet_values:
        result = feet_to_inches(value)
        print(f"{value} feet is {result} inches")