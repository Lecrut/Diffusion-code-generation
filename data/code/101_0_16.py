import datetime

def get_day_of_week(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.strftime('%A')
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(get_day_of_week(sample_date))