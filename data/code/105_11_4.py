from datetime import datetime, timedelta
def determine_next_date(start_date_str, days):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    next_date = start_date + timedelta(days=days)
    return next_date
if __name__ == '__main__':
    start_date_str_1 = "2023-01-01"
    days_1 = 365
    result_1 = determine_next_date(start_date_str_1, days_1)
    print(f"Start Date: {start_date_str_1}, Days: {days_1}, Result: {result_1}")
    start_date_str_2 = "2024-02-28"
    days_2 = 1
    result_2 = determine_next_date(start_date_str_2, days_2)
    print(f"Start Date: {start_date_str_2}, Days: {days_2}, Result: {result_2}")
    start_date_str_3 = "2024-02-28"
    days_3 = 2
    result_3 = determine_next_date(start_date_str_3, days_3)
    print(f"Start Date: {start_date_str_3}, Days: {days_3}, Result: {result_3}")
    start_date_str_4 = "2024-02-28"
    days_4 = 366
    result_4 = determine_next_date(start_date_str_4, days_4)
    print(f"Start Date: {start_date_str_4}, Days: {days_4}, Result: {result_4}")