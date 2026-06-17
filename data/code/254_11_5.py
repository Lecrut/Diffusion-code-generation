def find_minimum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"The minimum of {list1} is: {find_minimum(list1)}")
    list2 = [-10, 0, 5, -20, 3]
    print(f"The minimum of {list2} is: {find_minimum(list2)}")
    list3 = [42]
    print(f"The minimum of {list3} is: {find_minimum(list3)}")
    list4 = [100, 50, 25]
    print(f"The minimum of {list4} is: {find_minimum(list4)}")