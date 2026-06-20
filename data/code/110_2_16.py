from datetime import datetime

def is_valid_iso8601(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        return True
    except ValueError:
        return False

def sort_iso8601_dates(date_list):
    if not all(is_valid_iso8601(date) for date in date_list):
        raise ValueError("All dates must be in ISO 8601 format.")
    
    return sorted(date_list, key=lambda date: datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ"))

if __name__ == '__main__':
    sample_dates = ["2023-01-15T12:00:00.000Z", "2022-12-31T23:59:59.999Z", "2023-05-20T00:00:00.000Z"]
    sorted_dates = sort_iso8601_dates(sample_dates)
    print(sorted_dates)