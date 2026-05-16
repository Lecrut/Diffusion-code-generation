if __name__ == '__main__':
    data = [10, 55, 48, 100, 33, 60]
    flag = False
    for item in data:
        if item % 2 == 0 and item > 50:
            flag = True
            break
    print(flag)