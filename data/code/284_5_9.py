import random

def reverse_list(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[~i] = lst[~i], lst[i]
    return lst

if __name__ == '__main__':
    sample_list = [random.randint(1, 100) for _ in range(10)]
    print("Original list:", sample_list)
    reversed_list = reverse_list(sample_list.copy())
    print("Reversed list:", reversed_list)