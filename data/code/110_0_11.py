def sort_date_strings(date_list):
    try:
        return sorted(date_list, key=lambda date: tuple(map(int, date.split('-'))))
    except (ValueError, TypeError) as e:
        raise ValueError("Invalid date format in list") from e

if __name__ == '__main__':
    sample_dates = ['2023-04-01', '2022-01-15', '2023-03-20']
    print(sort_date_strings(sample_dates))