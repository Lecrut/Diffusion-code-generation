def ounces_to_grams(ounces):
    if not isinstance(ounces, (int, float)) or ounces < 0:
        raise ValueError("Invalid input: Ounces must be a non-negative number.")
    return ounces * 28.3495

if __name__ == '__main__':
    try:
        print(ounces_to_grams(16))
        print(ounces_to_grams(-1))
    except ValueError as e:
        print(e)