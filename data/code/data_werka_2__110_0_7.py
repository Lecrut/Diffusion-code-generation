from datetime import datetime

def sort_date_strings(date_list):
    if not date_list:
        return []
    return sorted(date_list, key=lambda d: datetime.strptime(d, '%Y-%m-%d'))

if __name__ == '__main__':
    unsorted_dates = ['2023-05-20', '1999-12-31', '2023-01-01', '2001-02-28']
    sorted_result = sort_date_strings(unsorted_dates)
    print(sorted_result)