def calculate_list_sum(iterable):
    total = 0
    for number in iterable:
        total += number
    return total

if __name__ == '__main__':
    sample1 = [5, 10, 15]
    sample2 = [-3, 0, 7, 4]
    sample3 = []
    print(f"Sum of {sample1}: {calculate_list_sum(sample1)}")
    print(f"Sum of {sample2}: {calculate_list_sum(sample2)}")
    print(f"Sum of {sample3}: {calculate_list_sum(sample3)}")