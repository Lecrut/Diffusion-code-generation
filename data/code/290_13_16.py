def tons_to_kilograms(tons):
    if not isinstance(tons, (int, float)) or tons < 0:
        raise ValueError("Input must be a non-negative number in tons")
    kilograms = tons * 907.184
    return round(kilograms, 2)

if __name__ == '__main__':
    sample_tons = [2.5, 3.75, 0.1, 10.0]
    for tons in sample_tons:
        print(tons_to_kilograms(tons))