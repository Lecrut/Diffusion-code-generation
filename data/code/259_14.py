import sys
if __name__ == '__main__':
    input_data = "10,5,22,8,15"
    numbers = [int(x.strip()) for x in input_data.split(',')]
    if numbers:
        smallest = min(numbers)
        largest = max(numbers)
        print(f"Smallest: {smallest}")
        print(f"Largest: {largest}")
    else:
        print("No numbers found")