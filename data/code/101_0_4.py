import datetime

def determine_day_of_week(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    day_index = date_obj.weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[day_index]

if __name__ == '__main__':
    sample_date = '2023-10-05'
    result = determine_day_of_week(sample_date)
    print(result)