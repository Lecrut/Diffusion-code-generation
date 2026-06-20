import datetime

def calculate_month_difference(date1, date2):
    try:
        if not isinstance(date1, datetime.date) or not isinstance(date2, datetime.date):
            raise ValueError('Both inputs must be datetime.date objects.')
        difference_in_years = date2.year - date1.year
        difference_in_months = difference_in_years * 12 + (date2.month - date1.month)
        return abs(difference_in_months)
    except Exception as e:
        print(f'Error: {e}')
        return None
if __name__ == '__main__':
    date1 = datetime.date(2023, 4, 15)
    date2 = datetime.date(2022, 8, 20)
    difference = calculate_month_difference(date1, date2)
    print(difference)