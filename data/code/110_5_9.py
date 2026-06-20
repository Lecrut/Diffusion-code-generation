from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%d/%m/%Y')
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")

def sort_dates(date_strings):
    parsed_dates = [parse_date(date_str) for date_str in date_strings]
    sorted_dates = sorted(parsed_dates)
    return [date.strftime('%d/%m/%Y') for date in sorted_dates]

if __name__ == '__main__':
    sample_dates = [
        "20/12/2022",
        "31/05/2023",
        "15/08/2021",
        "01/01/2024"
    ]
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)