def validate_date_format(date_str):
    if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
        raise ValueError("Date must be in YYYY-MM-DD format")
    for i in [0, 1, 2, 3, 5, 6, 8, 9]:
        if not date_str[i].isdigit():
            raise ValueError("Date must be in YYYY-MM-DD format")

def compare_dates(date_str1, date_str2):
    validate_date_format(date_str1)
    validate_date_format(date_str2)

    return (date_str1 > date_str2) - (date_str1 < date_str2)

if __name__ == '__main__':
    result = compare_dates("2023-10-26", "2023-10-25")
    print(f"Result: {result}")