def print_numbers():
    try:
        start = 0
        end = 10
        if not (isinstance(start, int) and isinstance(end, int)):
            raise ValueError("Start and end values must be integers")
        if start > end:
            raise ValueError("Start value must be less than or equal to end value")
        for i in range(start, end):
            print(i)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    print_numbers()