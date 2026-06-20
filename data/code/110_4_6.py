def validate_date_tuples(date_list):
    if not all(isinstance(item, tuple) and len(item) == 3 for item in date_list):
        raise ValueError("All items must be tuples of length 3")
    if not all(isinstance(year, int) and isinstance(month, int) and isinstance(day, int)
                for year, month, day in date_list):
        raise ValueError("All elements within tuples must be integers")

def sort_date_tuples(date_list):
    validate_date_tuples(date_list)
    return sorted(date_list)

if __name__ == '__main__':
    sample_dates = [(2023, 4, 5), (2022, 1, 1), (2023, 1, 15)]
    print(sort_date_tuples(sample_dates))