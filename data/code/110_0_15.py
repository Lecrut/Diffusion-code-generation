DATE_FORMAT = '%Y-%m-%d'

def sort_date_strings(date_list):
    return sorted(date_list, key=lambda date: datetime.strptime(date, DATE_FORMAT))

if __name__ == '__main__':
    sample_dates = ['2023-04-01', '2022-01-15', '2023-03-20']
    print(sort_date_strings(sample_dates))