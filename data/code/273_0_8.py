def repeat_action(action, times):
    if not callable(action):
        raise ValueError("action must be a callable function")
    for _ in range(times):
        action()

def sample_action():
    print("Action repeated")

if __name__ == '__main__':
    repeat_action(sample_action, 5)