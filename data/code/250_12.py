if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    total = 0
    count = 0
    for num in numbers:
        try:
            total += num
            count += 1
        except TypeError:
            print("Error: Invalid input detected. Please enter only numbers.")
            continue
    if count > 0:
        average = total / count
        print(f"The average of the entered numbers is: {average}")
    else:
        print("No valid numbers were entered to calculate the average.")