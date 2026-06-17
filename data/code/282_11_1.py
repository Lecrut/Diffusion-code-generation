import sys
if __name__ == '__main__':
    input_data = "10 20 30 40 50"
    numbers = []
    try:
        for item in input_data.split():
            numbers.append(int(item))
        total_sum = sum(numbers)
        print(total_sum)
    except ValueError:
        sys.stderr.write("Error: Invalid input detected.\n")