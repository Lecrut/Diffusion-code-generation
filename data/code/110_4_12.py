def sort_date_tuples(date_list):
    if not all(isinstance(date, tuple) and len(date) == 3 for date in date_list):
        raise ValueError("All elements must be tuples of length 3.")
    return sorted(date_list)

if __name__ == '__main__':
    sample_dates = [(2023, 1, 15), (2022, 12, 25), (2024, 1, 1)]
    try:
        sorted_dates = sort_date_tuples(sample_dates)
        print("Sorted Dates:")
        for date in sorted_dates:
            print(date)
    except ValueError as e:
        print(e)