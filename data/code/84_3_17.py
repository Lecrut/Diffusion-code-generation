from datetime import datetime

def day_of_year(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.timetuple().tm_yday
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_str}. Expected format is 'YYYY-MM-DD'") from e

if __name__ == '__main__':
    print(day_of_year('2023-10-27'))