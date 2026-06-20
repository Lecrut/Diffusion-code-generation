def calculate_months_difference(start_month, end_month):
    return abs(end_month - start_month)

if __name__ == '__main__':
    start = 1
    end = 6
    result1 = calculate_months_difference(start, end)
    print(f"Start: {start}, End: {end}, Difference: {result1}")
    
    start = 9
    end = 3
    result2 = calculate_months_difference(start, end)
    print(f"Start: {start}, End: {end}, Difference: {result2}")