import datetime

def convert_date(date_str):
    dt = datetime.datetime.strptime(date_str, "%m/%d/%Y")
    return dt.strftime("%Y-%m-%d")

if __name__ == '__main__':
    result = convert_date("12/31/2023")
    print(result)