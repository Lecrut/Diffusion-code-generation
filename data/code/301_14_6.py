from datetime import datetime

def standardize_dates(dates):
    standardized = []
    for date in dates:
        try:
            dt = datetime.strptime(date, '%m/%d/%Y')
            standardized.append(dt.strftime('%d/%m/%Y'))
        except ValueError:
            try:
                dt = datetime.strptime(date, '%Y-%m-%d')
                standardized.append(dt.strftime('%d/%m/%Y'))
            except ValueError:
                try:
                    dt = datetime.strptime(date, '%A, %B %d, %Y')
                    standardized.append(dt.strftime('%d/%m/%Y'))
                except ValueError:
                    standardized.append('Invalid date format')
    return standardized

if __name__ == '__main__':
    dates = ['12/31/2020', '2021-01-01', 'Monday, December 25, 2021']
    print(standardize_dates(dates))