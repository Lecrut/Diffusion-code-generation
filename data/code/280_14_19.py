def print_hello_world(times):
    if not isinstance(times, int) or times < 0:
        raise ValueError("Input must be a non-negative integer")
    
    for _ in range(times):
        print("Hello World!")

if __name__ == '__main__':
    try:
        num_times = 10
        print_hello_world(num_times)
    except ValueError as e:
        print(e)