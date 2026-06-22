def feet_to_inches(feet: float) -> float:
    if feet < 0:
        raise ValueError("Length in feet cannot be negative.")
    return feet * 12

if __name__ == '__main__':
    result = feet_to_inches(5)
    print(result)