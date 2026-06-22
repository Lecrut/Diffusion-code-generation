def print_hello_world(times):
    message = 'Hello World!'
    for _ in range(times):
        print(message)
if __name__ == '__main__':
    sample_values = {1: 2, 2: 3, 3: 4}
    repeat_times = sample_values[2]
    print_hello_world(repeat_times)