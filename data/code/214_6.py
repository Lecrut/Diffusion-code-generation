import sys
if __name__ == '__main__':
    input_data = "10 5 2 8 1"
    numbers = [int(x) for x in input_data.split()]
    if numbers:
        smallest = min(numbers)
        print(smallest)