def day_number_in_month(month):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month]
if __name__ == '__main__':
    print(day_number_in_month(4))