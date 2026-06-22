from dateutil.parser import parse

def get_day(date_str: str) -> int:
    if not date_str or not isinstance(date_str, str):
        raise ValueError("Invalid input")
    return parse(date_str).day

if __name__ == '__main__':
    date_input = "14-Feb-2024"
    day_value = get_day(date_input)
    print(day_value)