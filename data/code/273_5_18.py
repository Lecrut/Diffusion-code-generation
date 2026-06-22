MAX_RECURSION = 3

def repeat_action(action, n):
    if n <= 0:
        return
    action()
    repeat_action(action, n - 1)

if __name__ == '__main__':
    def sample_action():
        print("Action executed")

    repeat_count = MAX_RECURSION
    repeat_action(sample_action, repeat_count)