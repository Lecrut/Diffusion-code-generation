def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    maximum = data[0]
    for number in data[1:]:
        if number > maximum:
            maximum = number
    return maximum
if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2]
    sample_list2 = [-10, -5, -20, -1]
    sample_list3 = [7]
    sample_list4 = []
    print(f"Maximum of {sample_list1}: {find_maximum(sample_list1)}")
    print(f"Maximum of {sample_list2}: {find_maximum(sample_list2)}")
    print(f"Maximum of {sample_list3}: {find_maximum(sample_list3)}")
    try:
        find_maximum(sample_list4)
    except ValueError as e:
        print(f"Error for {sample_list4}: {e}")