import datetime

def calculate_date_difference(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    dates = {
        '01/15/2023': datetime.datetime(2023, 1, 15),
        '03/20/2023': datetime.datetime(2023, 3, 20),
        '12/31/2022': datetime.datetime(2022, 12, 31),
        '01/01/2023': datetime.datetime(2023, 1, 1)
    }
    
    date_a = dates['01/15/2023']
    date_b = dates['03/20/2023']
    print(f"Difference between {date_a} and {date_b}: {calculate_date_difference(date_a, date_b)} days")
    
    date_c = dates['12/31/2022']
    date_d = dates['01/01/2023']
    print(f"Difference between {date_c} and {date_d}: {calculate_date_difference(date_c, date_d)} days")