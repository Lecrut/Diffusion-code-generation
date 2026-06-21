from datetime import datetime

def sort_dates_chronologically(date_strings):
    if not date_strings:
        return []
    
    def validate_and_parse(date_str):
        parts = date_str.split('/')
        if len(parts) != 3:
            raise ValueError(f"Expected DD/MM/YYYY format: {date_str}")
        day_str, month_str, year_str = parts
        if not (day_str.isdigit() and month_str.isdigit() and year_str.isdigit()):
            raise ValueError(f"Non-numeric components in: {date_str}")
        day = int(day_str)
        month = int(month_str)
        year = int(year_str)
        if year < 1 or month < 1 or month > 12 or day < 1:
            raise ValueError(f"Invalid date range in: {date_str}")
        try:
            return datetime(year=year, month=month, day=day)
        except ValueError:
            raise ValueError(f"Invalid calendar date in: {date_str}")

    parsed_items = [(validate_and_parse(ds), ds) for ds in date_strings]
    parsed_items.sort(key=lambda x: x[0])
    return [item[1] for item in parsed_items]

if __name__ == '__main__':
    sample_dates = ['25/12/2023', '01/01/2024', '15/06/2023', '31/12/2022']
    sorted_dates = sort_dates_chronologically(sample_dates)
    print(sorted_dates)