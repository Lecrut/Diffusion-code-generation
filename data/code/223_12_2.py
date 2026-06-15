if __name__ == '__main__':
    numbers = [15, 8, 22, 4, 30, 11]
    if not numbers:
        print("The list is empty.")
    else:
        current_max = numbers[0]
        for number in numbers[1:]:
            if number > current_max:
                current_max = number
        print(f"The maximum value is: {current_max}")