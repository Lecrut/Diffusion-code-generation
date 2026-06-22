def repeat_action(action, times):
    if not isinstance(times, int) or times < 0:
        raise ValueError("Times must be a non-negative integer")
    for _ in range(times):
        action()

def sample_action():
    print("Action executed")

if __name__ == '__main__':
    try:
        repeat_action(sample_action, 10)
    except ValueError as e:
        print(e)