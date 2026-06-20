from datetime import datetime

def validate_iso_dates(date_strings):
    for date_str in date_strings:
        try:
            datetime.fromisoformat(date_str)
        except ValueError as e:
            raise ValueError(f"Invalid ISO 8601 date: {date_str}") from e

def sort_iso_dates(date_strings):
    validate_iso_dates(date_strings)
    return sorted(date_strings, key=lambda date: datetime.fromisoformat(date))

if __name__ == '__main__':
    sample_dates = [
        '2023-01-01T12:00:00Z',
        '2022-12-31T23:59:59Z',
        '2023-01-02T00:00:00Z'
    ]
    sorted_dates = sort_iso_dates(sample_dates)
    print(sorted_dates)