import datetime

def format_date(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    formatted_date = f"{date_obj.day} {date_obj.strftime('%B')} {date_obj.year}"
    return formatted_date

if __name__ == '__main__':
    sample_date = "2023-11-11"
    result = format_date(sample_date)
    print(result)