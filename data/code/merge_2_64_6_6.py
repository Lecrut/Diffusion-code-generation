import datetime
def format_date(date_obj: datetime.date) -> str:
    return date_obj.strftime("%B %d, %Y")
if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 1, 15),
        datetime.date(2024, 6, 30),
        datetime.datetime.now().date(),
    ]
    formatted_output = []
    for date in sample_dates:
        formatted_str = format_date(date)
        formatted_output.append(formatted_str)
    print("\n".join(formatted_output))