def find_maximum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_maximum(list1))
    list2 = [-10, -5, -20, -1]
    print(find_maximum(list2))
    list3 = [7]
    print(find_maximum(list3))
    list4 = []
    try:
        print(find_maximum(list4))
    except ValueError as e:
        print(e)