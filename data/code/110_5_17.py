from datetime import datetime

def sort_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        try:
            date_obj = datetime.strptime(date_str, '%d/%m/%Y')
            parsed_dates.append((date_obj, date_str))
        except ValueError:
            continue
    parsed_dates.sort()
    return [date_str for _, date_str in parsed_dates]

if __name__ == '__main__':
    sample_dates = [
        "20/11/2023",
        "05/12/2023",
        "15/10/2023"
    ]
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)