def find_maximum(numbers):
    if not numbers:
        return None
    max_element = numbers[0]
    for number in numbers[1:]:
        if number > max_element:
            max_element = number
    return max_element
if __name__ == '__main__':
    data1 = [10, 5, 20, 8]
    print(find_maximum(data1))
    data2 = [-5, -1, -10, -3]
    print(find_maximum(data2))
    data3 = []
    print(find_maximum(data3))