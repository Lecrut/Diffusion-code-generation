def validate_date_tuple(date_tuple):
    if not isinstance(date_tuple, (list, tuple)):
        raise ValueError("Date must be a tuple or list")
    if len(date_tuple) != 3:
        raise ValueError("Date must have exactly three elements")
    year, month, day = date_tuple
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Date components must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31")
    return True

def sort_date_tuples(dates):
    validated_dates = []
    for date in dates:
        validate_date_tuple(date)
        validated_dates.append(date)
    
    n = len(validated_dates)
    arr = list(validated_dates)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            curr = arr[j]
            ref = arr[min_idx]
            if curr[0] < ref[0]:
                min_idx = j
            elif curr[0] == ref[0]:
                if curr[1] < ref[1]:
                    min_idx = j
                elif curr[1] == ref[1]:
                    if curr[2] < ref[2]:
                        min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

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