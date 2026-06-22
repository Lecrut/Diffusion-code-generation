def feet_to_inches(feet: float) -> float:
    return feet * 12.0

if __name__ == '__main__':
    sample_feet = [1.0, 5.5, 0.25, 10.123456789]
    for f in sample_feet:
        result = feet_to_inches(f)
        print(result)