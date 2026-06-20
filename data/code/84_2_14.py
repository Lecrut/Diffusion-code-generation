import calendar

def day_of_year(year, month, day):
    if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
        raise ValueError("All inputs must be integers.")
    
    if not (1 <= year <= 9999) or not (1 <= month <= 12) or not (1 <= day <= calendar.monthrange(year, month)[1]):
        raise ValueError("Invalid date provided.")
    
    return sum(calendar.monthrange(year, m)[1] for m in range(1, month)) + day

if __name__ == '__main__':
    print(day_of_year(2023, 10, 27))