import sys
if __name__ == '__main__':
    input_data = "10 5 22 8 3"
    numbers = []
    try:
        input_list = input_data.split()
        if input_list:
            numbers = [int(x) for x in input_list]
        else:
            numbers = []
    except ValueError:
        numbers = []
    if numbers:
        largest = max(numbers)
        print(largest)
    else:
        print("No numbers provided")