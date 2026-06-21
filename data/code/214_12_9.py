def validate_input(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    for item in data:
        if not isinstance(item, float):
            raise TypeError("All items must be of type float")

def find_minimum(data):
    validate_input(data)
    minimum = data[0]
    for number in data[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    list1 = [3.14, 1.618, 2.718, 0.577]
    list2 = [-10.5, 5.2, -3.14, 9.9]
    list3 = [42.0]
    empty_list = []
    print(f"Minimum of {list1}: {find_minimum(list1)}")
    print(f"Minimum of {list2}: {find_minimum(list2)}")
    print(f"Minimum of {list3}: {find_minimum(list3)}")
    try:
        find_minimum(empty_list)
    except ValueError as e:
        print(e)