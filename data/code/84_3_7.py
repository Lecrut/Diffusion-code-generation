from datetime import datetime

def day_of_year(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.timetuple().tm_yday
    except ValueError:
        return None
if __name__ == '__main__':
    print(day_of_year('2023-10-27'))
    print(day_of_year('2023-13-01'))