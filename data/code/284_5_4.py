import random

def reverse_list(lst):
    length = len(lst)
    for i in range(length // 2):
        lst[i], lst[length - i - 1] = lst[length - i - 1], lst[i]

if __name__ == '__main__':
    sample_list = [random.randint(1, 100) for _ in range(10)]
    print("Original list:", sample_list)
    reverse_list(sample_list)
    print("Reversed list:", sample_list)