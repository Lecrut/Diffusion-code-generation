import sys
if __name__ == '__main__':
    try:
        length = int(sys.argv[1])
        width = int(sys.argv[2])
        perimeter = 2 * (length + width)
        print(perimeter)
    except IndexError:
        print("Usage: python script_name.py <length> <width>")
    except ValueError:
        print("Error: Length and width must be integers.")