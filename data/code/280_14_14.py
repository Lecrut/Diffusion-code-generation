def print_hello_world(times):
    if times < 0:
        raise ValueError("Number of repetitions must be non-negative.")
    
    for _ in range(times):
        print("Hello World!")

if __name__ == '__main__':
    try:
        number_of_repeats = 10
        print_hello_world(number_of_repeats)
    except ValueError as e:
        print(e)