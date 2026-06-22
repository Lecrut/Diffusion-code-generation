def is_valid_list(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    return True

def reverse_list_in_place(lst):
    is_valid_list(lst)
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

if __name__ == '__main__':
    sample_list = [random.randint(1, 100) for _ in range(10)]
    print("Original list:", sample_list)
    reverse_list_in_place(sample_list)
    print("Reversed list:", sample_list)