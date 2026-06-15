import random
def check_existence(number_list, target):
    return target in number_list
if __name__ == '__main__':
    sample_numbers = [1, 5, 10, 42, 7, 99]
    target_number = 42
    if check_existence(sample_numbers, target_number):
        print(f"The number {target_number} exists in the list.")
    else:
        print(f"The number {target_number} does not exist in the list.")