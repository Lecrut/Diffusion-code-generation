SAMPLE_DATES = [(2023, 1, 15), (2022, 12, 25), (2024, 1, 1)]

def sort_date_tuples(date_list):
    return sorted(date_list)
if __name__ == '__main__':
    sorted_dates = sort_date_tuples(SAMPLE_DATES)
    print('Sorted Dates:')
    for date in sorted_dates:
        print(f'{date[0]}-{date[1]:02d}-{date[2]:02d}')