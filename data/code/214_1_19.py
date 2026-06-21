def is_valid_number_list(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input must be a list of numbers")

def find_minimum(numbers):
    is_valid_number_list(numbers)
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, 50, -3]
    list3 = []
    list4 = [42]
    print(f"Minimum of {list1}: {find_minimum(list1)}")
    print(f"Minimum of {list2}: {find_minimum(list2)}")
    print(f"Minimum of {list3}: {find_minimum(list3)}")
    print(f"Minimum of {list4}: {find_minimum(list4)}")