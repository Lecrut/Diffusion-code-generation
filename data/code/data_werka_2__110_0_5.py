DATE_YEAR_INDEX = 0
DATE_MONTH_INDEX = 5
DATE_DAY_INDEX = 8
DATE_SEPARATOR = '-'

def sort_dates_chronologically(date_strings):
    def parse_date_to_tuple(date_str):
        year_part = date_str[DATE_YEAR_INDEX:DATE_YEAR_INDEX + 4]
        month_part = date_str[DATE_MONTH_INDEX:DATE_MONTH_INDEX + 2]
        day_part = date_str[DATE_DAY_INDEX:DATE_DAY_INDEX + 2]
        return (int(year_part), int(month_part), int(day_part))

    return sorted(date_strings, key=lambda d: parse_date_to_tuple(d))

if __name__ == '__main__':
    sample_dates = ['2023-10-01', '2021-05-15', '2022-01-01', '2023-01-01', '2020-02-29']
    sorted_dates = sort_dates_chronologically(sample_dates)
    print(sorted_dates)