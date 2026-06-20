import datetime

def calculate_date_difference(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date_a = datetime.datetime(2023, 1, 15)
    date_b = datetime.datetime(2023, 3, 20)
    print(f"Difference between {date_a.date()} and {date_b.date()}: {calculate_date_difference(date_a, date_b)} days")
    
    date_c = datetime.datetime(2022, 12, 31)
    date_d = datetime.datetime(2023, 1, 1)
    print(f"Difference between {date_c.date()} and {date_d.date()}: {calculate_date_difference(date_c, date_d)} days")
    
    date_e = datetime.datetime(2023, 10, 10)
    date_f = datetime.datetime(2023, 10, 25)
    print(f"Difference between {date_e.date()} and {date_f.date()}: {calculate_date_difference(date_e, date_f)} days")