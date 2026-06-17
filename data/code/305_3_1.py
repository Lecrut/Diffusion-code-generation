import datetime
def parse_dates(date_string):
    dates = []
    for line in date_string.strip().split('\n'):
        if line:
            try:
                dates.append(datetime.datetime.strptime(line.strip(), '%Y-%m-%d'))
            except ValueError:
                continue
    return sorted(dates)
if __name__ == '__main__':
    sample_dates = "2023-10-25\n2023-10-01\n2024-01-15\n2023-12-31"
    result = parse_dates(sample_dates)
    print(result)