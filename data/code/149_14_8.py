def validate_input(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    if not all(isinstance(item, (int, str)) for item in lst):
        raise ValueError("List items must be integers or strings")

def reverse_list(lst):
    validate_input(lst)
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)