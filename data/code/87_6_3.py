if __name__ == '__main__':
    data = [10, 55, 48, 60, 33, 72]
    flag_set = False
    for item in data:
        if item % 2 == 0 and item > 50:
            flag_set = True
            break
    print(flag_set)