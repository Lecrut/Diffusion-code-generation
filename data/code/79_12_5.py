from datetime import datetime, timedelta

def next_month_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    if date_obj.month == 12:
        return (date_obj.replace(year=date_obj.year + 1, month=1) + timedelta(days=30)).strftime('%Y-%m-%d')
    else:
        return (date_obj.replace(month=date_obj.month + 1) + timedelta(days=30)).strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(next_month_date('2023-04-15'))