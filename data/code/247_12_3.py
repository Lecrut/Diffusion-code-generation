import sys
def add_integers():
    try:
        a = int(sys.stdin.readline())
        b = int(sys.stdin.readline())
        result = a + b
        print(result)
    except ValueError:
        print("Error: Invalid input. Please enter integers.", file=sys.stderr)
    except EOFError:
        pass
if __name__ == '__main__':
    a = 10
    b = 25
    print(a + b)