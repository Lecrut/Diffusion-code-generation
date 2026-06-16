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
    sample_dates = "2023-10-26\n2023-10-24\n2023-10-25\n2023-10-27"
    sorted_dates = parse_dates(sample_dates)
    print(sorted_dates)