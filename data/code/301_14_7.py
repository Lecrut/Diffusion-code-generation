import datetime

def standardize_date(date_str):
    date_formats = {
        '%m/%d/%Y': '%d/%m/%Y',
        '%Y-%m-%d': '%d/%m/%Y',
        '%A, %B %d, %Y': '%d/%m/%Y'
    }
    for input_format, output_format in date_formats.items():
        try:
            return datetime.strptime(date_str, input_format).strftime(output_format)
        except ValueError:
            continue
    raise ValueError("Invalid date format provided.")

if __name__ == '__main__':
    sample_dates = [
        "10/27/2023",
        "2024-01-15",
        "Monday, February 29, 2024"
    ]
    for date in sample_dates:
        try:
            print(standardize_date(date))
        except ValueError as e:
            print(e)