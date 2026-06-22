def convert_pounds_to_kilograms(pounds):
    if not isinstance(pounds, (int, float)) or pounds < 0:
        raise ValueError("Invalid input: pounds must be a non-negative number")
    
    kilograms = pounds * 0.453592
    return kilograms

if __name__ == '__main__':
    sample_pounds = 10
    try:
        result_kilograms = convert_pounds_to_kilograms(sample_pounds)
        print(f"{sample_pounds} pounds is equal to {result_kilograms:.2f} kilograms")
    except ValueError as e:
        print(e)