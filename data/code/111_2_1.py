def extract_date_parts(date_string):
    try:
        year, month, day = map(int, date_string.split('-'))
        return year, month, day
    except ValueError:
        raise ValueError("Invalid date format. Expected 'YYYY-MM-DD'.")
if __name__ == '__main__':
    date1 = "2023-10-27"
    date2 = "1999-01-01"
    date3 = "2024-02-29"
    invalid_date1 = "2023/10/27"
    invalid_date2 = "2023-10-32"
    print(f"Processing {date1}: {extract_date_parts(date1)}")
    print(f"Processing {date2}: {extract_date_parts(date2)}")
    print(f"Processing {date3}: {extract_date_parts(date3)}")
    try:
        extract_date_parts(invalid_date1)
    except ValueError as e:
        print(f"Error processing {invalid_date1}: {e}")
    try:
        extract_date_parts(invalid_date2)
    except ValueError as e:
        print(f"Error processing {invalid_date2}: {e}")