if __name__ == '__main__':
    numbers = [12, 45, 78, 34, 56]
    min_number = min(numbers, key=lambda x: x)
    print(min_number)