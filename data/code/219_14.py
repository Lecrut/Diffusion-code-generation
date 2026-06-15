import sys
if __name__ == '__main__':
    data = [15, 8, 42, 3, 99, 27, 50]
    if not data:
        print("Error: Input list is empty")
    else:
        largest = data[0]
        for number in data[1:]:
            if number > largest:
                largest = number
        print(largest)