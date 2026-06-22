def sort_date_tuples(dates):
    def validate_input(dates_list):
        if not isinstance(dates_list, list):
            raise ValueError("Input must be a list")
        if len(dates_list) == 0:
            return
        for item in dates_list:
            if not isinstance(item, tuple):
                raise ValueError("Each item must be a tuple")
            if len(item) != 3:
                raise ValueError("Each tuple must have exactly 3 elements")
            year, month, day = item
            if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
                raise ValueError("Elements must be integers")
            if not (1 <= month <= 12):
                raise ValueError("Month must be between 1 and 12")
            if not (1 <= day <= 31):
                raise ValueError("Day must be between 1 and 31")
            if year < 1:
                raise ValueError("Year must be positive")

    def compare_dates(d1, d2):
        if d1[0] != d2[0]:
            return d1[0] - d2[0]
        if d1[1] != d2[1]:
            return d1[1] - d2[1]
        return d1[2] - d2[2]

    validate_input(dates)
    sorted_dates = list(dates)
    n = len(sorted_dates)
    for i in range(1, n):
        key = sorted_dates[i]
        j = i - 1
        while j >= 0 and compare_dates(sorted_dates[j], key) > 0:
            sorted_dates[j + 1] = sorted_dates[j]
            j -= 1
        sorted_dates[j + 1] = key
    return sorted_dates

if __name__ == '__main__':
    sample_dates = [
        (2023, 10, 15),
        (1999, 1, 1),
        (2023, 1, 1),
        (2023, 10, 1),
        (1999, 12, 31)
    ]
    sorted_dates = sort_date_tuples(sample_dates)
    print(sorted_dates)