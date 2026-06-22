from datetime import datetime

def transform_date(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%d.%m.%Y")
    return dt.strftime("%Y-%m-%d")

if __name__ == '__main__':
    print(transform_date("25.12.2023"))
    print(transform_date("01.01.2000"))
    print(transform_date("31.12.1999"))