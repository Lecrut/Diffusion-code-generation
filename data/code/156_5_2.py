if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    total = 0
    count = 0
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
            count += 1
        else:
            print(f"Invalid input found: {num}. Skipping.")
    if count > 0:
        average = total / count
        print(f"The numbers entered are: {numbers}")
        print(f"The calculated average is: {average}")
    else:
        print("No valid numbers were entered to calculate the average.")