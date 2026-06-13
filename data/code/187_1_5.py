import sys
if __name__ == '__main__':
    input_data = [10, 5, 20, 8, 15]
    if not input_data:
        print("List is empty")
    else:
        largest = input_data[0]
        for number in input_data:
            if number > largest:
                largest = number
        print(largest)