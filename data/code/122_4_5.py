import sys
if __name__ == '__main__':
    input_data = "10 20 30 40 50"
    numbers = []
    try:
        for item in input_data.split():
            numbers.append(int(item))
        if numbers:
            average = sum(numbers) / len(numbers)
            print(average)
        else:
            print("0")
    except ValueError:
        print("Error: Invalid input detected.")