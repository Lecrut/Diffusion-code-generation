from datetime import datetime

def years_difference(date1: str, date2: str) -> int:
    try:
        dt1 = datetime.strptime(date1, "%Y-%m-%d")
        dt2 = datetime.strptime(date2, "%Y-%m-%d")
        difference = abs((dt1 - dt2).days // 365)
        return difference
    except ValueError as e:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e

if __name__ == '__main__':
    date1 = "2023-04-15"
    date2 = "1998-07-20"
    try:
        diff = years_difference(date1, date2)
        print(f"Date 1: {date1}")
        print(f"Date 2: {date2}")
        print(f"The difference in years is: {diff}")
    except ValueError as e:
        print(e)