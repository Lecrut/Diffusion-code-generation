MAX_RECURSION = 3

def repeat_action(action, n):
    if n <= 0:
        return
    action()
    repeat_action(action, n - 1)

def sample_action():
    print("Action executed")

if __name__ == '__main__':
    repeat_action(sample_action, MAX_RECURSION)