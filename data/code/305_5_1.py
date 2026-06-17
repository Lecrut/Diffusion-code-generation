from datetime import datetime
def parse_and_sort_dates(date_strings):
    valid_dates = []
    for date_str in date_strings:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            valid_dates.append(date_obj)
        except ValueError:
            pass
    valid_dates.sort()
    return valid_dates
if __name__ == '__main__':
    sample_dates = [
        "2023-01-15",
        "2023-12-31",
        "2023/01/01",
        "2023-02-29",
        "invalid-date",
        "2023-03-10"
    ]
    sorted_dates = parse_and_sort_dates(sample_dates)
    print(sorted_dates)