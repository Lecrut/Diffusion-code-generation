import calendar

def month_difference(month1: str, month2: str) -> int:
    months = list(calendar.month_name[1:])
    index1 = months.index(month1)
    index2 = months.index(month2)
    return abs(index1 - index2)

if __name__ == '__main__':
    print(month_difference('January', 'March'))