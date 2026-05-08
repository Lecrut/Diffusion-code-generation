import sys
if __name__ == '__main__':
    input_data = "10 5 20 1 15"
    try:
        numbers = list(map(int, input_data.split()))
        if numbers:
            largest = max(numbers)
            print(largest)
        else:
            print("List is empty")
    except ValueError:
        print("Invalid input: Please ensure all inputs are integers.")