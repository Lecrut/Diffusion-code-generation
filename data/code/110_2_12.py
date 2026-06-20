from datetime import datetime

def iso8601_to_timestamp(date_str):
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z").timestamp()

def sort_iso8601_dates(date_list):
    return sorted(date_list, key=iso8601_to_timestamp)

if __name__ == '__main__':
    sample_dates = [
        '2023-04-01T12:00:00+01:00',
        '2023-03-31T23:59:59-01:00',
        '2023-04-02T00:00:00Z'
    ]
    sorted_dates = sort_iso8601_dates(sample_dates)
    print(sorted_dates)