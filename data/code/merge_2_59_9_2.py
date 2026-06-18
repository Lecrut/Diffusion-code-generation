import datetime
def parse_date_to_weekday(date_str):
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%y%m%d",
        "dd.mm.yyyy"
    ]
    for fmt in formats:
        try:
            date_obj = datetime.datetime.strptime(date_str, fmt)
            weekday_name = date_obj.strftime("%A")
            return {"status": "success", "date": date_str, "weekday": weekday_name}
        except ValueError as e:
            continue
    error_msg = f"Invalid date format '{date_str}'. Supported formats include YYYY-MM-DD, DD/MM/YYYY, Month DD, YYYY, YYMMDD, and dd.mm.yyyy."
    return {"status": "error", "message": error_msg}
if __name__ == '__main__':
    sample_inputs = [
        "2023-10-05",
        "05/10/2023",
        "October 05, 2023",
        "231005",
        "05.10.2023",
        "not a date"
    ]
    for input_date in sample_inputs:
        result = parse_date_to_weekday(input_date)
        print(f"Input: {input_date}")
        if result["status"] == "success":
            print(f"Weekday: {result['weekday']}")
        else:
            print(result["message"])