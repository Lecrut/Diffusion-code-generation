import sys
if __name__ == '__main__':
    input_data = "10 20 30 40 50"
    numbers = list(map(int, input_data.split()))
    if numbers:
        mean = sum(numbers) / len(numbers)
        print(mean)
    else:
        print("The list of numbers is empty.")