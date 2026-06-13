import sys
if __name__ == '__main__':
    input_data = "10 5 20 8 15"
    try:
        numbers = list(map(int, input_data.split()))
        if numbers:
            largest = max(numbers)
            print(largest)
        else:
            pass
    except ValueError:
        pass