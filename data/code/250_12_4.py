if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    total = 0
    valid_numbers = []
    for item in numbers:
        try:
            number = float(item)
            valid_numbers.append(number)
            total += number
        except ValueError:
            print(f"Skipping invalid input: {item}")
    if valid_numbers:
        average = total / len(valid_numbers)
        print(f"The numbers entered are: {valid_numbers}")
        print(f"The average is: {average}")
    else:
        print("No valid numbers were entered.")