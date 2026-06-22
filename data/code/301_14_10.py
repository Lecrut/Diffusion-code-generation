from datetime import datetime

def standardize_dates(date_list):
    standardized_dates = []
    for date in date_list:
        try:
            if '/' in date:
                dt = datetime.strptime(date, '%m/%d/%Y')
            elif '-' in date:
                dt = datetime.strptime(date, '%Y-%m-%d')
            else:
                dt = datetime.strptime(date, '%A, %B %d, %Y')
            standardized_dates.append(dt.strftime('%d/%m/%Y'))
        except ValueError:
            standardized_dates.append('Invalid Date')
    return standardized_dates

if __name__ == '__main__':
    sample_dates = ['12/31/2020', '2021-01-01', 'Monday, January 04, 2021']
    print(standardize_dates(sample_dates))