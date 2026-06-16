import datetime
def parse_and_sort_dates(date_string):
    dates = []
    for line in date_string.strip().split('\n'):
        if line:
            try:
                dates.append(datetime.datetime.strptime(line.strip(), '%Y-%m-%d'))
            except ValueError:
                continue
    dates.sort()
    return dates
if __name__ == '__main__':
    sample_input = "2023-10-26\n2023-10-25\n2023-10-27\n2023-10-24"
    result = parse_and_sort_dates(sample_input)
    print(result)