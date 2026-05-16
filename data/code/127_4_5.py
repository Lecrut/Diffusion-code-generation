import sys
if __name__ == '__main__':
    input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for num in input_data:
        try:
            if num % 2 == 0:
                print("Even")
            else:
                print("Odd")
        except TypeError:
            print("Error: Invalid input type encountered.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")