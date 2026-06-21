def get_day(date_str):
    if len(date_str) != 10:
        raise ValueError("Invalid date format")
    if date_str[4] != '-' or date_str[7] != '-':
        raise ValueError("Invalid date format")
    if not (date_str[:4].isdigit() and date_str[5:7].isdigit() and date_str[8:10].isdigit()):
        raise ValueError("Invalid date format")
    return date_str[8:10]

if __name__ == '__main__':
    print(get_day("2023-10-05"))