from datetime import datetime

DATE_FORMAT = '%d/%m/%Y'

MONTH_NAMES = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
}

def sort_dates_chronologically(date_strings):
    parsed = []
    for ds in date_strings:
        dt = datetime.strptime(ds, DATE_FORMAT)
        parsed.append((dt, ds))
    parsed.sort(key=lambda x: x[0])
    return [item[1] for item in parsed]

if __name__ == '__main__':
    raw_dates = ['31/01/2023', '15/02/2023', '01/01/2023', '28/02/2023']
    sorted_list = sort_dates_chronologically(raw_dates)
    print(sorted_list)