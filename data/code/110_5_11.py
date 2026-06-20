from datetime import datetime

def sort_dates(date_strings):
    try:
        parsed_dates = [datetime.strptime(date_str, '%d/%m/%Y') for date_str in date_strings]
        return sorted(parsed_dates)
    except ValueError as e:
        print(f"Invalid date format: {e}")
        return []

if __name__ == '__main__':
    sample_dates = [
        "20/12/2023",
        "01/01/2023",
        "15/08/2023",
        "31/07/2023"
    ]
    sorted_dates = sort_dates(sample_dates)
    for date in sorted_dates:
        print(date.strftime('%d/%m/%Y'))