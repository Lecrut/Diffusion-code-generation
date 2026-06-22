from datetime import timedelta

def compute_day_difference(start_day, start_month, start_year, end_day, end_month, end_year):
    start_date = timedelta(days=0).replace(year=start_year, month=start_month, day=start_day)
    end_date = timedelta(days=0).replace(year=end_year, month=end_month, day=end_day)
    difference = end_date - start_date
    return difference.days

if __name__ == '__main__':
    s_d = 1
    s_m = 1
    s_y = 2023
    e_d = 31
    e_m = 12
    e_y = 2023
    diff = compute_day_difference(s_d, s_m, s_y, e_d, e_m, e_y)
    print(diff)