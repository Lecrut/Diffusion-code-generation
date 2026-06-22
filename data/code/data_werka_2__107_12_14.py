import datetime

def convert_date(date_str: str) -> str:
    parsed_date = datetime.datetime.strptime(date_str, "%d-%b-%Y")
    return parsed_date.strftime("%Y%m%d")

if __name__ == '__main__':
    sample_date = "01-Jan-2023"
    result = convert_date(sample_date)
    print(result)