from datetime import datetime

def years_difference(date1: str, date2: str) -> int:
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    return abs((d2 - d1).days // 365)

if __name__ == '__main__':
    print(years_difference("2020-01-01", "2023-04-15"))