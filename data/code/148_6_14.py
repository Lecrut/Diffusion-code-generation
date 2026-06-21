def find_largest(data):
    if not data:
        raise ValueError("Cannot find the largest element in an empty list.")
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    sample_list1 = [1, 5, 2, 8, 3]
    sample_list2 = []
    sample_list3 = [-10, -5, -20]

    try:
        print(f"The largest element in {sample_list1} is: {find_largest(sample_list1)}")
    except ValueError as e:
        print(e)

    try:
        print(f"The largest element in {sample_list2} is: {find_largest(sample_list2)}")
    except ValueError as e:
        print(e)

    try:
        print(f"The largest element in {sample_list3} is: {find_largest(sample_list3)}")
    except ValueError as e:
        print(e)