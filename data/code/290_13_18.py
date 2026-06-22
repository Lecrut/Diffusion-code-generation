def tons_to_kilograms(tons):
    if not isinstance(tons, (int, float)) or tons < 0:
        raise ValueError("Input must be a non-negative number")
    return round(tons * 907.184, 2)

if __name__ == '__main__':
    sample_tons = [2.5, 3.75, 0.1, 10.0]
    for tons in sample_tons:
        try:
            kilograms = tons_to_kilograms(tons)
            print(f"{tons} ton(s) is equal to {kilograms} kg")
        except ValueError as e:
            print(e)