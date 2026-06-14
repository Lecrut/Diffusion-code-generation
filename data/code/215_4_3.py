def determine_maximum(numbers):
    if not numbers:
        raise ValueError("Input iterable cannot be empty")
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum
if __name__ == '__main__':
    list1 = [10, 4, 20, 5, 30]
    list2 = [-5, -1, -10, -2]
    list3 = [7]
    empty_list = []
    print(f"Maximum of {list1}: {determine_maximum(list1)}")
    print(f"Maximum of {list2}: {determine_maximum(list2)}")
    print(f"Maximum of {list3}: {determine_maximum(list3)}")
    try:
        determine_maximum(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")