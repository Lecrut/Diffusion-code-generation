def pounds_to_kilograms(pounds):
    if not isinstance(pounds, (int, float)) or pounds < 0:
        raise ValueError("Invalid input. Please provide a non-negative number in pounds.")
    return pounds * 0.453592

if __name__ == '__main__':
    sample_pounds = 10.0
    try:
        result_kg = pounds_to_kilograms(sample_pounds)
        print(f"{sample_pounds} lbs is {result_kg:.2f} kg")
    except ValueError as e:
        print(e)