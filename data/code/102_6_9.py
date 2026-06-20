def is_weekday(day_index):
    return 0 <= day_index < 5
if __name__ == '__main__':
    print(is_weekday(3))
    print(is_weekday(6))