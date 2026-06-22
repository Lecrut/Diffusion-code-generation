def days_remaining(year):
    try:
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer")
        
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        days_in_february = 29 if is_leap_year else 28
        
        return days_in_february
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    year = 2024
    print(days_remaining(year))