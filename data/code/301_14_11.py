from datetime import datetime

def standardize_dates(dates):
    standardized = []
    for date in dates:
        try:
            parsed_date = datetime.strptime(date, '%m/%d/%Y')
        except ValueError:
            try:
                parsed_date = datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                parsed_date = datetime.strptime(date, '%A, %B %d, %Y')
        standardized.append(parsed_date.strftime('%d/%m/%Y'))
    return standardized

if __name__ == '__main__':
    sample_dates = ['12/31/2020', '2021-01-01', 'Monday, January 04, 2021']
    print(standardize_dates(sample_dates))