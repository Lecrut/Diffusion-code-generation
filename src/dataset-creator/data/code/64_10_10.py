import datetime
def convert_date_to_full_month_name(date_string):
    try:
        formats = [
            "%Y-%m-%d",
            "%d/%m/%Y",
            "%B %d, %Y",
            "%y%m%d",
            "dd-mm-yyyy"
        ]
        for fmt in formats:
            try:
                date_obj = datetime.datetime.strptime(date_string, fmt)
                return f"{date_obj.strftime('%A')} {date_obj.month} of the year {date_obj.year}"
            except ValueError:
                continue
    except Exception as e:
        pass
    raise ValueError(f"Unable to parse '{date_string}' into a valid date format")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "05/10/2023",
        "October 5, 2023",
        "231005",
        "05-10-2023"
    ]
    for date_str in sample_dates:
        try:
            result = convert_date_to_full_month_name(date_str)
            print(f"{date_str} -> {result}")
        except ValueError as ve:
            print(f"Error processing '{date_str}': {ve}")