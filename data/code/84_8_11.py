from datetime import datetime

DAYS_IN_YEAR = 365

def calculate_day_of_year(date_str):
    date_format = "%Y-%m-%d"
    date_obj = datetime.strptime(date_str, date_format)
    day_of_year = date_obj.timetuple().tm_yday
    return day_of_year

if __name__ == '__main__':
    sample_date_1 = "2023-04-15"
    result_1 = calculate_day_of_year(sample_date_1)
    print(f"Date: {sample_date_1}, Day of Year: {result_1}")

    sample_date_2 = "2023-12-31"
    result_2 = calculate_day_of_year(sample_date_2)
    print(f"Date: {sample_date_2}, Day of Year: {result_2}")

    sample_date_3 = "2024-01-01"
    result_3 = calculate_day_of_year(sample_date_3)
    print(f"Date: {sample_date_3}, Day of Year: {result_3}")