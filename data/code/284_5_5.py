import random

def reverse_list(input_list):
    length = len(input_list)
    for i in range(length // 2):
        input_list[i], input_list[length - i - 1] = input_list[length - i - 1], input_list[i]

if __name__ == '__main__':
    sample_list = [random.randint(1, 50) for _ in range(7)]
    print("Original list:", sample_list)
    reverse_list(sample_list)
    print("Reversed list:", sample_list)