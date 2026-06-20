DATE_FORMAT = "%Y-%m-%d"

def date_tuple_to_str(date_tuple):
    return f"{date_tuple[0]}-{date_tuple[1]:02}-{date_tuple[2]:02}"

def sort_date_tuples(date_list):
    return sorted(map(date_tuple_to_str, date_list), key=lambda x: x)

if __name__ == '__main__':
    sample_dates = [(2023, 4, 5), (2022, 1, 1), (2023, 1, 15)]
    sorted_dates = sort_date_tuples(sample_dates)
    print([tuple(map(int, date_str.split('-'))) for date_str in sorted_dates])