if __name__ == '__main__':
    input_value = 10
    try:
        number = int(input_value)
        if number > 0:
            print("Positive")
        else:
            print("Not Positive")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")