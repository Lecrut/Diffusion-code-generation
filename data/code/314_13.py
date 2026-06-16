if __name__ == '__main__':
    input_string = "10,25,33,error,42"
    numbers = []
    for item in input_string.split(','):
        try:
            numbers.append(int(item.strip()))
        except ValueError:
            print(f"Skipping non-numeric value: {item}")
    total_sum = sum(numbers)
    print(f"The total sum is: {total_sum}")