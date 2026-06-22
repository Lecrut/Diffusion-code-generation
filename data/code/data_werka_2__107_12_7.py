import datetime

def convert_date(date_string: str) -> str:
    parsed_date = datetime.datetime.strptime(date_string, "%d-%b-%Y")
    return parsed_date.strftime("%Y%m%d")

if __name__ == '__main__':
    sample_date = "25-Dec-2023"
    result = convert_date(sample_date)
    print(result)