import sys
if __name__ == '__main__':
    input_data = "10 5 -3 22 8"
    numbers = []
    for item in input_data.split():
        numbers.append(int(item))
    if not numbers:
        print("No numbers provided.")
    else:
        minimum = min(numbers)
        maximum = max(numbers)
        print(f"Minimum: {minimum}")
        print(f"Maximum: {maximum}")