import datetime

def format_date(date_string: str) -> str:
    date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    return date_obj.strftime("%d/%m/%Y")

if __name__ == '__main__':
    result = format_date("2023-10-25")
    print(result)