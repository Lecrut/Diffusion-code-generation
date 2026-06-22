def day_number(month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month - 1]
if __name__ == '__main__':
    print(day_number(2))