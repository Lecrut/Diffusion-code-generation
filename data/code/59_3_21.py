def find_middle_element(lst):
    return lst[len(lst) // 2]

if __name__ == '__main__':
    example_list = [10, 20, 30, 40, 50]
    middle_value = find_middle_element(example_list)
    print(f"The middle element is: {middle_value}")