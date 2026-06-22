from dateutil.parser import parse

def extract_weekday(date_string: str) -> str:
    parsed_datetime = parse(date_string)
    weekday_index = parsed_datetime.weekday()
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return day_names[weekday_index]

if __name__ == '__main__':
    input_date = 'January 15, 2023'
    output = extract_weekday(input_date)
    print(output)