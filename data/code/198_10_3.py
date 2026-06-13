import sys
if __name__ == '__main__':
    input_data = [42, 15, 89, 3, 77, 20]
    if not input_data:
        print("List is empty")
    else:
        smallest = input_data[0]
        for number in input_data[1:]:
            if number < smallest:
                smallest = number
        print(smallest)