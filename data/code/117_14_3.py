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
    list1 = [10, 5, 20, 15, 8]
    list2 = [-5, 100, 0, -20]
    list3 = [3.14, 1.618, 2.718]
    list4 = []
    list5 = [5000000, 1, 9999999]
    print(f"List 1 range: {calculate_range(list1)}")
    print(f"List 2 range: {calculate_range(list2)}")
    print(f"List 3 range: {calculate_range(list3)}")
    print(f"List 4 range: {calculate_range(list4)}")
    print(f"List 5 range: {calculate_range(list5)}")