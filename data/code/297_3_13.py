def pounds_to_kilograms(pounds):
    if not isinstance(pounds, (int, float)) or pounds < 0:
        raise ValueError("Input must be a non-negative number in pounds.")
    return pounds * 0.453592

if __name__ == '__main__':
    sample_pounds = 10
    result_kg = pounds_to_kilograms(sample_pounds)
    print(result_kg)