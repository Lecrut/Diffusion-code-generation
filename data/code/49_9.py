import sys
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <length1> <length2>")
    else:
        try:
            length1 = float(sys.argv[1])
            length2 = float(sys.argv[2])
            if length1 < 0 or length2 < 0:
                print("Error: Lengths must be non-negative.")
            else:
                print(f"Length 1: {length1}")
                print(f"Length 2: {length2}")
                if length1 == length2:
                    print("Comparison Result: The lengths are equal.")
                elif length1 > length2:
                    difference = length1 - length2
                    print(f"Comparison Result: Length 1 is greater than Length 2 by {difference}.")
                else:
                    difference = length2 - length1
                    print(f"Comparison Result: Length 2 is greater than Length 1 by {difference}.")
        except ValueError:
            print("Error: Both arguments must be valid numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")