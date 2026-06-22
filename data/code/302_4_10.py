def day_number(month):
    return (month - 1) * 30 + 1
if __name__ == '__main__':
    print(day_number(2))
    print(day_number(4))
    print(day_number(7))