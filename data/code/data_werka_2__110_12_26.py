from datetime import date

def sort_date_tuples(dates):
    if not dates:
        return []
    result = []
    for d in dates:
        if not isinstance(d, (list, tuple)) or len(d) != 3:
            raise ValueError("Each date must be a tuple or list of 3 integers (year, month, day)")
        year, month, day = d
        if not all(isinstance(x, int) for x in d):
            raise ValueError("Each date component must be an integer")
        try:
            date_obj = date(year, month, day)
        except ValueError as e:
            raise ValueError(f"Invalid date components: {d}") from e
        result.append(date_obj)
    result.sort()
    return [(d.year, d.month, d.day) for d in result]

if __name__ == '__main__':
    sample_dates = [
        (2024, 2, 29),
        (2023, 2, 28),
        (2024, 2, 28),
        (2023, 12, 1),
        (2023, 1, 1)
    ]
    sorted_dates = sort_date_tuples(sample_dates)
    print(sorted_dates)