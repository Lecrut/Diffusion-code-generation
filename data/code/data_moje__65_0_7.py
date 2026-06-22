def feet_to_inches(feet: float) -> float:
    return feet * 12

if __name__ == '__main__':
    sample_feet = 5
    result = feet_to_inches(sample_feet)
    print(result)
    sample_feet2 = 10.5
    result2 = feet_to_inches(sample_feet2)
    print(result2)