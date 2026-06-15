if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    total = 0
    count = 0
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
            count += 1
        else:
            print(f"Error: '{num}' is not a valid number. Skipping.")
    if count > 0:
        average = total / count
        print(f"The average of the entered numbers is: {average}")
    else:
        print("No valid numbers were entered to calculate the average.")