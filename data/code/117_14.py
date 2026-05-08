def calculate_range(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    maximum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    return maximum - minimum
if __name__ == '__main__':
    list1 = [10, 5, 20, 15, 30]
    list2 = [-5, 100, 0, -20]
    list3 = [7]
    list4 = []
    print(calculate_range(list1))
    print(calculate_range(list2))
    print(calculate_range(list3))
    print(calculate_range(list4))