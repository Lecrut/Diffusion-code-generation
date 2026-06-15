import sys
if __name__ == '__main__':
    input_data = "10 5 20 3 15"
    numbers = []
    try:
        for item in input_data.split():
            numbers.append(int(item))
    except ValueError:
        pass
    if not numbers:
        print("No numbers provided.")
    else:
        maximum = numbers[0]
        for number in numbers[1:]:
            if number > maximum:
                maximum = number
        print(maximum)