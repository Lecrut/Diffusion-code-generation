def sum_list(lst):
    if not isinstance(lst, list) or not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Input must be a list of numbers")
    return sum(lst) if lst else 0

if __name__ == '__main__':
    print(sum_list([10, 20, 30, 40]))
    print(sum_list([]))