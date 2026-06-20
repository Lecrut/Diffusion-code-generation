from datetime import datetime

def sort_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        try:
            date_obj = datetime.strptime(date_str, '%d/%m/%Y')
            parsed_dates.append((date_obj, date_str))
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}")
    parsed_dates.sort()
    return [date_str for _, date_str in parsed_dates]

if __name__ == '__main__':
    sample_dates = [
        "20/12/2023",
        "01/01/2024",
        "15/08/2023",
        "31/12/2022"
    ]
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)