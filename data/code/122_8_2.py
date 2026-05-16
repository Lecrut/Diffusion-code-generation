if __name__ == '__main__':
    input_string = "10,20,30,40,50"
    try:
        number_strings = input_string.split(',')
        numbers = [float(num.strip()) for num in number_strings]
        if numbers:
            average = sum(numbers) / len(numbers)
            print(average)
        else:
            print("No numbers found.")
    except ValueError:
        print("Error: Invalid input. Please ensure all parts are valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")