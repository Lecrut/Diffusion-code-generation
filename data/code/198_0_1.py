import sys
if __name__ == '__main__':
    input_data = [42, 15, 89, 3, 77, 22]
    if not input_data:
        print("Error: Input list is empty.")
    else:
        smallest = min(input_data)
        print(smallest)