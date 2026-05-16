import sys
if __name__ == '__main__':
    input_data = [10, 5, 22, 8, 30, 15]
    if not input_data:
        print("List is empty")
    else:
        largest = input_data[0]
        for number in input_data[1:]:
            if number > largest:
                largest = number
        print(largest)