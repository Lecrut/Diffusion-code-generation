import re

PATTERN = re.compile(r'^(\d{4})-(\d{2})-(\d{2})$')

def get_day_component(date_str: str) -> str:
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    match = PATTERN.match(date_str)
    if not match:
        raise ValueError(f"Invalid date format: {date_str}")
    return match.group(3)

if __name__ == '__main__':
    date_input = "2023-10-05"
    day_result = get_day_component(date_input)
    print(day_result)