import sys
if __name__ == '__main__':
    input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for num in input_data:
        try:
            if isinstance(num, int):
                if num % 2 == 0:
                    print("Even")
                else:
                    print("Odd")
            else:
                print(f"Error: Invalid input type for {num}")
        except TypeError:
            print(f"Error: Could not process value {num}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")