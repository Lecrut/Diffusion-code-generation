from datetime import datetime

def format_date(date_str: str) -> str:
    parsed_date = datetime.strptime(date_str, "%d-%b-%Y")
    return parsed_date.strftime("%Y%m%d")

if __name__ == "__main__":
    sample_date = "15-Jan-2023"
    result = format_date(sample_date)
    print(result)