def get_later_date(date1: str, date2: str) -> str:
    def validate_and_convert(date_str: str) -> int:
        if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
            raise ValueError("Invalid date format")
        year = int(date_str[0:4])
        month = int(date_str[5:7])
        day = int(date_str[8:10])
        if not (1 <= month <= 12):
            raise ValueError("Invalid month")
        if not (1 <= day <= 31):
            raise ValueError("Invalid day")
        return year * 10000 + month * 100 + day

    d1_val = validate_and_convert(date1)
    d2_val = validate_and_convert(date2)

    if d1_val >= d2_val:
        return date1
    return date2

if __name__ == '__main__':
    result = get_later_date("2023-10-15", "2023-10-16")
    print(result)