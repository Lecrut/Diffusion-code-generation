def find_smallest_in_list(data_list):
    if not data_list:
        raise ValueError("Input list cannot be empty.")
    return min(data_list)

if __name__ == '__main__':
    list1 = [3.14, 1.618, 2.718, 0.5]
    print(f"List 1: {list1}")
    print(f"Smallest in List 1: {find_smallest_in_list(list1)}")