from datetime import datetime

class DateUtils:
    EPOCH = datetime(1970, 1, 1)
    
    @staticmethod
    def calculate_day_of_year(date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        days_since_epoch = (date_obj - DateUtils.EPOCH).days + 1
        day_of_year = (days_since_epoch - 1) % 365 + 1
        return day_of_year

if __name__ == '__main__':
    date_1 = '2023-04-10'
    result_1 = DateUtils.calculate_day_of_year(date_1)
    print(f"Date: {date_1}, Day of Year: {result_1}")
    
    date_2 = '2024-02-29'
    result_2 = DateUtils.calculate_day_of_year(date_2)
    print(f"Date: {date_2}, Day of Year: {result_2}")
    
    date_3 = '2025-12-31'
    result_3 = DateUtils.calculate_day_of_year(date_3)
    print(f"Date: {date_3}, Day of Year: {result_3}")