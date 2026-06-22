def print_hello_world(times):
    if not isinstance(times, int) or times < 0:
        raise ValueError("Number of repetitions must be a non-negative integer")
    
    for _ in range(times):
        print("Hello World!")

if __name__ == '__main__':
    try:
        number_of_times = 10
        print_hello_world(number_of_times)
    except ValueError as e:
        print(e)