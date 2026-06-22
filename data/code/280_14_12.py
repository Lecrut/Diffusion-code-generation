def print_hello_world(times):
    if not isinstance(times, int) or times < 0:
        raise ValueError("The number of times must be a non-negative integer.")
    
    for _ in range(times):
        print("Hello World!")

if __name__ == '__main__':
    try:
        print_hello_world(10)
    except ValueError as e:
        print(e)