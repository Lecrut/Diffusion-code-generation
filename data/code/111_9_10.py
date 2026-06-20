import datetime

def format_date(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return f"{date_obj.day} {date_obj.strftime('%B')} {date_obj.year}"
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    sample_date = "2022-11-11"
    formatted_date = format_date(sample_date)
    print(formatted_date)