from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'

def sort_dates_chronologically(date_strings):
    if not isinstance(date_strings, list):
        raise ValueError("Input must be a list")
    validated_dates = []
    for date_str in date_strings:
        if not isinstance(date_str, str):
            raise ValueError(f"Expected string, got {type(date_str).__name__}")
        try:
            parsed = datetime.strptime(date_str, DATE_FORMAT)
            validated_dates.append((parsed, date_str))
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}")
    validated_dates.sort(key=lambda x: x[0])
    return [item[1] for item in validated_dates]

if __name__ == '__main__':
    sample_dates = ['2023-10-01', '2021-05-15', '2022-01-01', '2023-01-01', '2000-12-25']
    result = sort_dates_chronologically(sample_dates)
    print(result)