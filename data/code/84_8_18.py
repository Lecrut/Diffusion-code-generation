from datetime import datetime

def calculate_day_of_year(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.timetuple().tm_yday

if __name__ == '__main__':
    date_1 = '2023-04-10'
    result_1 = calculate_day_of_year(date_1)
    print(f"Date: {date_1}, Day of Year: {result_1}")

    date_2 = '2023-12-31'
    result_2 = calculate_day_of_year(date_2)
    print(f"Date: {date_2}, Day of Year: {result_2}")

    date_3 = '2024-01-01'
    result_3 = calculate_day_of_year(date_3)
    print(f"Date: {date_3}, Day of Year: {result_3}")