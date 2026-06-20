def is_valid_date(date_str):
    if len(date_str) != 10:
        return False
    if date_str[4] != '-' or date_str[7] != '-':
        return False
    try:
        year = int(date_str[:4])
        month = int(date_str[5:7])
        day = int(date_str[8:])
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        return True
    except ValueError:
        return False

def calculate_year_difference(date_str1, date_str2):
    if not is_valid_date(date_str1) or not is_valid_date(date_str2):
        raise ValueError("Invalid input. Please enter dates in YYYY-MM-DD format.")
    
    year1 = int(date_str1[:4])
    year2 = int(date_str2[:4])
    return abs(year1 - year2)

if __name__ == '__main__':
    date1 = '2023-04-15'
    date2 = '1998-12-25'
    try:
        difference = calculate_year_difference(date1, date2)
        print(difference)
    except ValueError as e:
        print(e)