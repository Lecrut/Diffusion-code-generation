import datetime

def compare_dates(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d').date()
        return tuple(sorted([date1, date2]))
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2023-10-20"
    print(compare_dates(date_a, date_b))