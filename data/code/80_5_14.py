def compare_dates(date_str1, date_str2):
    return (date_str1 > date_str2) - (date_str1 < date_str2)

if __name__ == '__main__':
    result = compare_dates('2023-10-26', '2023-10-25')
    print(result)