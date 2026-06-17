def repeat_action(action, repetitions):
    for _ in range(repetitions):
        action()
if __name__ == '__main__':
    def print_hello():
        print("Hello")
    print_hello()
    repeat_action(print_hello, 3)