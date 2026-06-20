from datetime import datetime

def calculate_year_difference(date1: str, date2: str) -> int:
    try:
        dt1 = datetime.strptime(date1, '%Y-%m-%d')
        dt2 = datetime.strptime(date2, '%Y-%m-%d')
        return abs((dt1 - dt2).days // 365)
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

if __name__ == '__main__':
    date1 = "2023-04-01"
    date2 = "1998-07-15"
    try:
        difference = calculate_year_difference(date1, date2)
        print(f"Date 1: {date1}")
        print(f"Date 2: {date2}")
        print(f"The absolute difference in years is: {difference}")
    except ValueError as e:
        print(e)