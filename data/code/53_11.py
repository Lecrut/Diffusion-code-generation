import sys
if __name__ == '__main__':
    try:
        side_length = float(sys.stdin.read().strip())
        area = side_length * side_length
        print(area)
    except ValueError:
        pass