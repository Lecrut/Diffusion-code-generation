def feet_to_inches(feet: int | float) -> int | float:
    return feet * 12

if __name__ == '__main__':
    sample_values = [1, 5.5, 10, 0.25]
    for value in sample_values:
        result = feet_to_inches(value)
        print(result)