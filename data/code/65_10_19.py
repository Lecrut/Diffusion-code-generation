def feet_to_inches(feet: float) -> float:
    if not isinstance(feet, (int, float)):
        raise TypeError("feet must be a number")
    if feet < 0:
        raise ValueError("feet must be non-negative")
    return feet * 12

if __name__ == '__main__':
    sample_feet = 5.5
    result = feet_to_inches(sample_feet)
    print(result)

    sample_feet_2 = 0
    result_2 = feet_to_inches(sample_feet_2)
    print(result_2)

    sample_feet_3 = 10
    result_3 = feet_to_inches(sample_feet_3)
    print(result_3)