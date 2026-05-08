import sys
if __name__ == '__main__':
    input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for line in input_data:
        try:
            if line % 2 == 0:
                print("Even")
            else:
                print("Odd")
        except TypeError:
            print("Error: Invalid input encountered.")
        except Exception:
            print("An unexpected error occurred.")