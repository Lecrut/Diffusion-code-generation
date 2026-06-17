if __name__ == '__main__':
    data = [10, 5, 20, 3, 15]
    max_value = -float('inf')
    for num in data:
        if num > max_value:
            max_value = num
    print(max_value)