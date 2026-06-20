from datetime import datetime

def transform_date(date_str):
    return date_str.replace('.', '-')

if __name__ == '__main__':
    test_cases = [
        ('01.02.2023', '2023-02-01'),
        ('15.10.2021', '2021-10-15'),
        ('31.12.2020', '2020-12-31')
    ]
    
    for input_date, expected_output in test_cases:
        result = transform_date(input_date)
        print(f"Input: {input_date}, Expected Output: {expected_output}, Actual Output: {result}")