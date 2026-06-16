import datetime
def sort_dates(date_string):
    dates = []
    for line in date_string.strip().split('\n'):
        if line:
            try:
                dates.append(datetime.datetime.strptime(line.strip(), '%Y-%m-%d'))
            except ValueError:
                continue
    return sorted(dates)
if __name__ == '__main__':
    sample_input = "2023-10-26\n2023-10-24\n2023-10-25"
    result = sort_dates(sample_input)
    print(result)