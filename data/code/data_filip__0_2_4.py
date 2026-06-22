import re

def extract_digits(mixed_string: str) -> tuple:
    matches = re.findall(r'\d+', mixed_string)
    return tuple(int(num) for num in matches)

if __name__ == '__main__':
    sample_data = "Order #42 contains items A1, B99, and C305 in the year 2024."
    result = extract_digits(sample_data)
    print(result)