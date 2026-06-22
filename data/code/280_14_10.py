def print_hello_world(n):
    if n == 0:
        return
    print("Hello World!")
    print_hello_world(n - 1)

if __name__ == '__main__':
    times = 10
    if times < 0:
        raise ValueError("Number of repetitions must be non-negative")
    print_hello_world(times)