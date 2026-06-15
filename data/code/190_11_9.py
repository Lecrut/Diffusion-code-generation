import random
def check_existence(numbers, target):
    return target in numbers
if __name__ == '__main__':
    sample_numbers = [10, 25, 33, 42, 56, 78, 91]
    target_number = 42
    if check_existence(sample_numbers, target_number):
        print(f"The number {target_number} exists in the list.")
    else:
        print(f"The number {target_number} does not exist in the list.")