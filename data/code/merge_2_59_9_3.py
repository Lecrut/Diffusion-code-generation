import datetime
def parse_date_and_get_weekday(date_str):
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%y/%m/%d",
        "dd-mm-yyyy"
    ]
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"No valid date format found for input: {date_str}")
def get_weekday_name(dt):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return dt.strftime("%A")
if __name__ == '__main__':
    sample_inputs = [
        "2023-10-05",
        "05/10/2023",
        "October 05, 2023",
        "23/10/2024",
        "invalid-date-string"
    ]
    for input_date in sample_inputs:
        try:
            dt = parse_date_and_get_weekday(input_date)
            weekday_name = get_weekday_name(dt)
            print(f"Input: {input_date} -> Weekday: {weekday_name}")
        except ValueError as e:
            print(f"Error processing '{input_date}': {e}")