from datetime import datetime

def sort_dates(date_strings):
    date_format = '%d/%m/%Y'
    parsed_dates = [(datetime.strptime(date_str, date_format), index) for index, date_str in enumerate(date_strings)]
    sorted_dates = sorted(parsed_dates)
    return [date_str for date_obj, index in sorted_dates]

if __name__ == '__main__':
    sample_dates = [
        "20/12/2023",
        "05/09/2023",
        "25/06/2023",
        "18/03/2023"
    ]
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)