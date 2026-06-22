NUM_REPETITIONS = 5

def repeat_n_times(func):
    def wrapper(*args, **kwargs):
        for _ in range(NUM_REPETITIONS):
            func(*args, **kwargs)
    return wrapper

@repeat_n_times
def greet(name):
    print(f"Hello, {name}")

if __name__ == '__main__':
    greet("Alice")