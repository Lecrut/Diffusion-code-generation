def print_evens(start: int = 1, end: int = 20, step: int = 2):
    if not (isinstance(start, int) and isinstance(end, int) and isinstance(step, int)):
        raise ValueError("All parameters must be integers.")
    
    for num in range(start, end + 1, step):
        if num % 2 == 0:
            print(num)

if __name__ == '__main__':
    try:
        print_evens()
    except Exception as e:
        print(f"An error occurred: {e}")