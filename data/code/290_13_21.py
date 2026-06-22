def tons_to_kilograms(tons):
    if not isinstance(tons, (int, float)) or tons < 0:
        raise ValueError("Input must be a non-negative number in tons.")
    return round(tons * 907.184, 2)

if __name__ == '__main__':
    sample_tons = [1.5, 10.25, 500.75, -1, 'abc']
    for tons in sample_tons:
        try:
            print(f"{tons} tons is {tons_to_kilograms(tons)} kilograms")
        except ValueError as e:
            print(e)