from datetime import datetime

def sort_dates_chronologically(date_strings):
    def parse_date(date_str):
        parts = date_str.split('/')
        if len(parts) != 3:
            raise ValueError(f"Invalid date format: {date_str}")
        day_str, month_str, year_str = parts
        if not (day_str.isdigit() and month_str.isdigit() and year_str.isdigit()):
            raise ValueError(f"Invalid date format: {date_str}")
        day = int(day_str)
        month = int(month_str)
        year = int(year_str)
        return datetime(year=year, month=month, day=day)

    if not date_strings:
        return []

    validated_dates = []
    for ds in date_strings:
        dt_obj = parse_date(ds)
        validated_dates.append((dt_obj, ds))

    validated_dates.sort(key=lambda x: x[0])

    return [item[1] for item in validated_dates]

if __name__ == '__main__':
    sample_dates = ['10/05/2021', '01/01/2020', '31/12/2021', '15/02/2020']
    sorted_result = sort_dates_chronologically(sample_dates)
    print(sorted_result)