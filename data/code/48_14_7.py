def find_max_custom():
    numbers = [3.14, 1.59, 2.65, 3.58, 9.79, 3.23, 8.46]
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    result = find_max_custom()
    print(result)