from datetime import datetime
WEEK_START_DAY = 0

def dates_in_same_week(date1_str, date2_str):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    def get_week_number(date_obj):
        return (date_obj.isocalendar()[1] - 1) % 52 + 1
    week_num1 = get_week_number(date1)
    week_num2 = get_week_number(date2)
    return week_num1 == week_num2
if __name__ == '__main__':
    print(dates_in_same_week('2023-10-01', '2023-10-07'))
    print(dates_in_same_week('2023-10-01', '2023-10-08'))