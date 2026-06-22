def find_max_element(numbers):
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    data = [3.14, 2.71, 1.41, 9.99, 5.55]
    result = find_max_element(data)
    print(result)