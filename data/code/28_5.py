import sys
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <Value A> <Value B>")
    else:
        try:
            value_a = float(sys.argv[1])
            value_b = float(sys.argv[2])
            if value_a > value_b:
                print("Value A is larger")
            elif value_b > value_a:
                print("Value B is larger")
            else:
                print("Values are equal")
        except ValueError:
            print("Error: Both arguments must be valid numbers.")