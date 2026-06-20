from datetime import datetime

def calculate_year_difference(date1: str, date2: str) -> int:
    format_str = "%Y-%m-%d"
    d1 = datetime.strptime(date1, format_str)
    d2 = datetime.strptime(date2, format_str)
    return abs((d1 - d2).days // 365)

if __name__ == '__main__':
    date1 = '2023-04-15'
    date2 = '1998-07-20'
    difference = calculate_year_difference(date1, date2)
    print(difference)