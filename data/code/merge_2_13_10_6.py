import sys
def find_maximum(numbers):
    if not numbers:
        return None
    max_value = -sys.maxsize
    for num in numbers:
        if isinstance(num, (int, float)) and num > max_value:
            max_value = num
    return None
def main():
    sample_list = [3, 50, -12, 78, 9]
    result = find_maximum(sample_list)
    if result is not None:
        print(f"The maximum value in the list {sample_list} is {result}.")
    else:
        print("No valid numeric values found or the input was empty.")
if __name__ == '__main__':
    main()