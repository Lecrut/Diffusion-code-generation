if __name__ == '__main__':
    numbers = [10, 5, 20, 3, 15]
    valid_numbers = []
    for item in numbers:
        if isinstance(item, (int, float)):
            valid_numbers.append(item)
    if valid_numbers:
        minimum = min(valid_numbers)
        print(minimum)
    else:
        print("No valid numbers found in the list.")