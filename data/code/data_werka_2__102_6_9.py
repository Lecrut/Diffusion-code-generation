def is_weekday(day_index):
    return 0 <= day_index <= 4

if __name__ == '__main__':
    print(is_weekday(0))
    print(is_weekday(5))
    print(is_weekday(6))