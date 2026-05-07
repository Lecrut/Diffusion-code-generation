import datetime
def get_day_of_year(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.timetuple().tm_yday
    except ValueError:
        return None
if __name__ == '__main__':
    date1 = '2023-10-27'
    date2 = '1999-01-01'
    date3 = '2024-02-29'
    invalid_date1 = '27/10/2023'
    invalid_date2 = '2023-13-01'
    print(f"Date: {date1}, Day of Year: {get_day_of_year(date1)}")
    print(f"Date: {date2}, Day of Year: {get_day_of_year(date2)}")
    print(f"Date: {date3}, Day of Year: {get_day_of_year(date3)}")
    print(f"Date: {invalid_date1}, Day of Year: {get_day_of_year(invalid_date1)}")
    print(f"Date: {invalid_date2}, Day of Year: {get_day_of_year(invalid_date2)}")