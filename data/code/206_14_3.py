import sys
if __name__ == '__main__':
    input_data = "10 5 -3 22 1"
    numbers = []
    is_numeric = True
    for item in input_data.split():
        try:
            number = float(item)
            numbers.append(number)
        except ValueError:
            is_numeric = False
            break
    if is_numeric and numbers:
        print(min(numbers))
    else:
        pass