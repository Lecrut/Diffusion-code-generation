def month_difference(start_month, end_month):
    return abs(end_month - start_month)

if __name__ == '__main__':
    start = 1
    end = 8
    result1 = month_difference(start, end)
    print(f"Start: {start}, End: {end}, Difference: {result1}")
    
    start = 12
    end = 3
    result2 = month_difference(start, end)
    print(f"Start: {start}, End: {end}, Difference: {result2}")