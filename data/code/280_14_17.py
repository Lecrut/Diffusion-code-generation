def print_hello_world(times):
    if not isinstance(times, int) or times < 0:
        raise ValueError("The number of repetitions must be a non-negative integer.")
    
    for _ in range(times):
        print("Hello World!")

if __name__ == '__main__':
    try:
        number_of_repeats = 10
        print_hello_world(number_of_repeats)
    except Exception as e:
        print(f"An error occurred: {e}")