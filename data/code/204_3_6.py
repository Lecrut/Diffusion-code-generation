if __name__ == '__main__':
    input_str = "10,20,30,40,50"
    try:
        numbers = [int(x.strip()) for x in input_str.split(',')]
        if not numbers:
            print("Error: No numbers provided.")
        else:
            if len(numbers) % 2 == 1:
                middle_index = len(numbers) // 2
                print(numbers[middle_index])
            else:
                middle_right_index = len(numbers) // 2
                middle_left_index = middle_right_index - 1
                print((numbers[middle_left_index] + numbers[middle_right_index]) / 2)
    except ValueError:
        print("Error: Invalid input. Please ensure all inputs are integers separated by commas.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")