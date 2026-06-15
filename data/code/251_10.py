import sys
if __name__ == '__main__':
    input_data = [42, 10, 99, 5, 123, 78]
    if not input_data:
        print("Error: Input list is empty")
    else:
        largest = input_data[0]
        for number in input_data[1:]:
            if number > largest:
                largest = number
        print(largest)