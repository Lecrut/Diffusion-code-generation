import random
def check_existence(number_list, target):
    if target in number_list:
        print(f"{target} exists in the list.")
    else:
        print(f"{target} does not exist in the list.")
if __name__ == '__main__':
    sample_numbers = [1, 5, 10, 42, 8, 99]
    target_number = 42
    check_existence(sample_numbers, target_number)