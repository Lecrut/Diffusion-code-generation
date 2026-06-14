def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    maximum = data[0]
    for number in data[1:]:
        if number > maximum:
            maximum = number
    return maximum
if __name__ == '__main__':
    sample_list_1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"The maximum of {sample_list_1} is: {find_maximum(sample_list_1)}")
    sample_list_2 = [-10, -5, -20, -1]
    print(f"The maximum of {sample_list_2} is: {find_maximum(sample_list_2)}")
    sample_list_3 = [42]
    print(f"The maximum of {sample_list_3} is: {find_maximum(sample_list_3)}")
    sample_list_4 = [100, 50, 200, 75]
    print(f"The maximum of {sample_list_4} is: {find_maximum(sample_list_4)}")