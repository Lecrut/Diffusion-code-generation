def is_leap_year(year: int) -> bool:
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
def validate_input(year_value):
    try:
        return int(float(year_value)) if not isinstance(year_value, (int, float)) else int(year_value)
    except (ValueError, TypeError):
        raise ValueError("Input must be a valid number representing a year.")
if __name__ == '__main__':
    test_cases = [
        2000,                                     
        1900,                                                       
        2024,                                               
        2023,                                             
        -876                                                                 
    ]
    print("Leap Year Checker Results:")
    for test_year in test_cases:
        try:
            validated = validate_input(test_year)
            result = is_leap_year(validated)
            status = "LEAP YEAR" if result else "NOT A LEAP YEAR"
            print(f"{test_year}: {status}")
        except ValueError as e:
            print(f"Error processing input '{test_year}': {e}")
    invalid_inputs = ["abc", 20.5, None]
    for invalid_input in invalid_inputs:
        try:
            validated = validate_input(invalid_input)
            result = is_leap_year(validated)
            print(f"Unexpected success with '{invalid_input}': {result}")
        except ValueError as e:
            print(f"Correctly caught error for input type of '{type(invalid_input).__name__}': {e}")