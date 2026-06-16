def repeat_function(func, n):
    for i in range(n):
        func()
def sample_function():
    print("Function called.")
if __name__ == '__main__':
    repeat_function(sample_function, 3)