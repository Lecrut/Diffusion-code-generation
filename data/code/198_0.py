import sys
if __name__ == '__main__':
    input_data = [15, 3, 8, 22, 1]
    if not input_data:
        print("Error: Input list is empty")
    else:
        smallest = min(input_data)
        print(smallest)