import random
def check_number_existence(numbers, target):
    if target in numbers:
        print(f"{target} exists in the list.")
    else:
        print(f"{target} does not exist in the list.")
if __name__ == '__main__':
    sample_list = [1, 5, 10, 15, 22, 30]
    target_number = 42
    check_number_existence(sample_list, target_number)