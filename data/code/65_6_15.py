def feet_to_inches(feet: float) -> float:
    return feet * 12.0

if __name__ == '__main__':
    sample_values = [0.0, 1.0, 5.5, 10.25, -3.7]
    for value in sample_values:
        result = feet_to_inches(value)
        print(result)