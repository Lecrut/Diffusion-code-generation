from datetime import datetime
def parse_and_sort_dates(date_strings):
    valid_dates = []
    for date_str in date_strings:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            valid_dates.append(date_obj)
        except ValueError:
            continue
    valid_dates.sort()
    return valid_dates
if __name__ == '__main__':
    sample_dates = [
        "2023-01-15",
        "2022/12/31",
        "2023-03-01",
        "invalid-date",
        "2023-01-15"
    ]
    sorted_dates = parse_and_sort_dates(sample_dates)
    print(sorted_dates)