import datetime
def parse_date_to_weekday(date_string):
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%y/%m/%d",
        "dd.mm.yyyy"
    ]
    for fmt in formats:
        try:
            date_obj = datetime.datetime.strptime(date_string, fmt)
            weekday_name = date_obj.strftime("%A")
            return {"status": "success", "date": date_string, "weekday": weekday_name}
        except ValueError as e:
            continue
    raise ValueError(f"Invalid date format for input '{date_string}'. Supported formats include YYYY-MM-DD, DD/MM/YYYY, Month DD, YYYY, YY/MM/DD, or dd.mm.yyyy")
if __name__ == '__main__':
    sample_inputs = [
        "2023-10-27",
        "27/10/2023",
        "October 27, 2023",
        "23/10/2024",
        "invalid-date"
    ]
    for input_date in sample_inputs:
        try:
            result = parse_date_to_weekday(input_date)
            print(f"Input: {input_date} -> Weekday: {result['weekday']}")
        except ValueError as e:
            print(f"Error processing '{input_date}': {e}")