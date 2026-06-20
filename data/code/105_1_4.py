def first_sunday_after_jan_1():
    target_date = 2024
    while True:
        current_date = target_date * 365 + (target_date // 4) - (target_date // 100) + (target_date // 400)
        if current_date % 7 == 0:
            break
        target_date += 1
    return target_date

if __name__ == '__main__':
    first_sunday = first_sunday_after_jan_1()
    print(first_sunday)