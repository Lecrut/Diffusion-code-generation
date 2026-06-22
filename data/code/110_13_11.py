from datetime import datetime

def sort_iso_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        try:
            dt = datetime.fromisoformat(date_str)
            parsed_dates.append((dt, date_str))
        except ValueError:
            raise ValueError(f"Invalid ISO 8601 date string: {date_str}")
    
    parsed_dates.sort(key=lambda x: x[0])
    
    return [item[1] for item in parsed_dates]

if __name__ == '__main__':
    dates = [
        "2023-10-01T12:00:00",
        "2022-05-15T08:30:00",
        "2024-01-20T18:45:00",
        "2023-10-01T09:00:00"
    ]
    sorted_dates = sort_iso_dates(dates)
    print(sorted_dates)