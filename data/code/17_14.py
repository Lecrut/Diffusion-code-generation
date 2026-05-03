import sys
if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            number = int(sys.argv[1])
            if number % 2 == 0:
                print("Even")
            else:
                print("Odd")
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")
    else:
        sample_numbers = [4, 7, 0, -3]
        for num in sample_numbers:
            if num % 2 == 0:
                print(f"{num}: Even")
            else:
                print(f"{num}: Odd")