CASE_MAP = {
    'lower': str.lower,
    'upper': str.upper
}

def transform_string(s: str) -> tuple:
    upper_case = CASE_MAP['upper'](s)
    lower_case = CASE_MAP['lower'](s)
    return upper_case, lower_case

if __name__ == '__main__':
    sample_string = "HeLlO wOrLd"
    upper_result, lower_result = transform_string(sample_string)
    print(f"Original: {sample_string}")
    print(f"Uppercase: {upper_result}")
    print(f"Lowercase: {lower_result}")