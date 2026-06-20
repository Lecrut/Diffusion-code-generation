from datetime import datetime

def are_same_day(date_str1: str, date_str2: str) -> bool:
    try:
        date1 = datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.strptime(date_str2, '%Y-%m-%d')
        return date1.date() == date2.date()
    except ValueError:
        return False

if __name__ == '__main__':
    date_a = '2023-10-26'
    date_b = '2023-10-26'
    date_c = '2023-10-27'
    
    print(f"Date A: {date_a}")
    print(f"Date B: {date_b}")
    print(f"Date C: {date_c}")
    print(f"A and B are same day: {are_same_day(date_a, date_b)}")
    print(f"A and C are same day: {are_same_day(date_a, date_c)}")
    print(f"B and C are same day: {are_same_day(date_b, date_c)}")