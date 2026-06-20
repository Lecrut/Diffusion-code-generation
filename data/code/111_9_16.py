import datetime

def format_date(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return f"{date_obj.day} {date_obj.strftime('%B')} {date_obj.year}"

if __name__ == '__main__':
    sample_date = "2023-10-27"
    formatted_date = format_date(sample_date)
    print(formatted_date)