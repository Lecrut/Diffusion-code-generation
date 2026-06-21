if __name__ == '__main__':
    numbers = [10, 23, 45, 60, 78, 90]
    for number in numbers:
        if number % 2 == 0:
            continue
        if number > 50:
            break
        print(number)