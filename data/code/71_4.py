if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    if not numbers:
        print("The list is empty.")
    else:
        n = len(numbers)
        middle_index = n // 2
        middle_element = numbers[middle_index]
        print(middle_element)