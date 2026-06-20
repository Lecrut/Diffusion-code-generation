from datetime import datetime

def sort_dates(date_strings):
    date_formats = [
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d.%m.%Y"
    ]
    dates = []
    for date_str in date_strings:
        for fmt in date_formats:
            try:
                date_obj = datetime.strptime(date_str, fmt)
                dates.append((date_obj, date_str))
                break
            except ValueError:
                continue
    dates.sort()
    return [date[1] for date in dates]

if __name__ == '__main__':
    sample_dates = ["2023-01-01", "01/02/2023", "03.04.2022"]
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)