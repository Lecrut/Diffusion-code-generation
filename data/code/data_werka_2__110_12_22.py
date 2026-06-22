def sort_date_tuples(dates):
    if not isinstance(dates, (list, tuple)):
        raise ValueError("Input must be a list or tuple of date tuples")
    
    validated_dates = []
    for d in dates:
        if not isinstance(d, (list, tuple)):
            raise ValueError("Each date must be a tuple or list")
        if len(d) != 3:
            raise ValueError("Each date must have exactly 3 elements (year, month, day)")
        y, m, dy = d
        if not (isinstance(y, int) and isinstance(m, int) and isinstance(dy, int)):
            raise ValueError("Date components must be integers")
        validated_dates.append((y, m, dy))
    
    n = len(validated_dates)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            curr_y, curr_m, curr_dy = validated_dates[j]
            min_y, min_m, min_dy = validated_dates[min_idx]
            
            if (curr_y, curr_m, curr_dy) < (min_y, min_m, min_dy):
                min_idx = j
        
        if min_idx != i:
            validated_dates[i], validated_dates[min_idx] = validated_dates[min_idx], validated_dates[i]
    
    return validated_dates

if __name__ == '__main__':
    sample_dates = [
        (2023, 10, 15),
        (1999, 1, 1),
        (2023, 1, 1),
        (2023, 10, 1),
        (1999, 12, 31)
    ]
    result = sort_date_tuples(sample_dates)
    print(result)