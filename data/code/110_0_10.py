def is_valid_date(date):
    try:
        int(date[:4])
        int(date[5:7])
        int(date[8:])
        return True
    except ValueError:
        return False

def sort_date_strings(date_list):
    if not all((is_valid_date(date) for date in date_list)):
        raise ValueError("All elements in the list must be valid 'YYYY-MM-DD' date strings.")
    return sorted(date_list, key=lambda date: (int(date[:4]), int(date[5:7]), int(date[8:])))
if __name__ == '__main__':
    sample_dates = ['2023-04-01', '2022-01-15', '2023-03-20']
    print(sort_date_strings(sample_dates))