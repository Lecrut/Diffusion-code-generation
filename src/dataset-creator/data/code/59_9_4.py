import datetime
def parse_date_to_weekday(date_str):
    supported_formats = [
        "%Y-%m-%d",                  
        "%d/%m/%Y",                  
        "%m/%d/%Y",                  
        "%B %d, %Y",                       
        "%b %d, %Y",                   
        "%d-%m-%Y",                  
    ]
    for fmt in supported_formats:
        try:
            date_obj = datetime.datetime.strptime(date_str, fmt)
            weekday_name = date_obj.strftime("%A")
            return {"status": "success", "date": date_obj, "weekday": weekday_name}
        except ValueError as e:
            continue
    error_msg = f"Invalid date format '{date_str}'. Supported formats include YYYY-MM-DD, DD/MM/YYYY, MM/DD/YYYY, Month DD, YYYY."
    return {"status": "error", "message": error_msg}
if __name__ == '__main__':
    test_dates = [
        "2023-10-05",
        "05/10/2023",
        "October 05, 2023",
        "invalid-date-format",
        "99/99/2023"
    ]
    for date_input in test_dates:
        result = parse_date_to_weekday(date_input)
        print(f"Input: {date_input}")
        if result["status"] == "success":
            print(f"Weekday: {result['weekday']}")
        else:
            print(f"Error: {result['message']}")
        print("-" * 40)