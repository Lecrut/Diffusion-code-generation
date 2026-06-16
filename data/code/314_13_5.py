if __name__ == '__main__':
    input_string = "10,25,3,40"
    numbers = input_string.split(',')
    total_sum = 0
    for item in numbers:
        try:
            total_sum += int(item.strip())
        except ValueError:
            print(f"Error: '{item}' is not a valid integer.")
            exit(1)
    print(total_sum)