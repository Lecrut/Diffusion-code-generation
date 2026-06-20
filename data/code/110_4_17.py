def sort_date_tuples(date_list):
    if not all(isinstance(date, tuple) and len(date) == 3 and isinstance(y, int) and isinstance(m, int) and isinstance(d, int)
                for date in date_list for y, m, d in [date]):
        raise ValueError("All elements must be tuples of three integers representing (year, month, day)")
    return sorted(date_list)

if __name__ == '__main__':
    sample_dates = [(2023, 1, 15), (2022, 12, 25), (2024, 1, 1)]
    print(sort_date_tuples(sample_dates))