import datetime
def parse_and_standardize_dates(date_strings):
    standardized_dates = {}
    for original_format, date_strings_list in date_strings.items():
        for date_str in date_strings_list:
            try:
                date_obj = datetime.datetime.strptime(date_str, original_format)
                standardized_dates[date_str] = date_obj
            except ValueError:
                standardized_dates[date_str] = None
    return standardized_dates
if __name__ == '__main__':
    input_data = {
        "format_1": ["2023-01-15", "2023/01/16"],
        "format_2": ["01/16/2023", "16-Jan-2023"],
        "format_3": ["2023-01-17"]
    }
    results = parse_and_standardize_dates(input_data)
    print(results)