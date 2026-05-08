import sys
if __name__ == '__main__':
    input_data = [10, 5, 20, 15, 30]
    if not input_data:
        print("Error: Input list is empty")
    else:
        largest_value = input_data[0]
        for number in input_data:
            if number > largest_value:
                largest_value = number
        print(largest_value)