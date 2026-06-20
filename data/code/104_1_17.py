def later_date(date1: str, date2: str) -> str:
    d1 = [int(x) for x in date1.split('-')]
    d2 = [int(x) for x in date2.split('-')]
    if d1 > d2:
        return date1
    else:
        return date2

if __name__ == '__main__':
    print(later_date('2023-10-05', '2023-09-15'))