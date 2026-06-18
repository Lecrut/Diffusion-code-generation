import datetime
def format_date(date_obj: datetime.date) -> str:
    return date_obj.strftime("%B %d, %Y")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "1998-07-20",
        "2045-12-31"
    ]
    output_results = []
    for date_str in sample_dates:
        try:
            parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            formatted_string = format_date(parsed_date)
            output_results.append(formatted_string)
        except ValueError as e:
            print(f"Error parsing {date_str}: {e}")
    for result in output_results:
        print(result)