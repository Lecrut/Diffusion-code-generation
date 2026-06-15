import sys
if __name__ == '__main__':
    input_data = [10, 5, 22, 8, 30]
    if not input_data:
        largest_number = None
    else:
        largest_number = max(input_data)
    print(largest_number)