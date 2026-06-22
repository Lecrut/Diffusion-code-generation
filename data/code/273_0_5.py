def repeat_sequence(action):
    if not callable(action):
        raise ValueError("action must be a callable function")
    for _ in range(5):
        action()

if __name__ == '__main__':
    def sample_action():
        print("Action repeated")
    
    try:
        repeat_sequence(sample_action)
    except ValueError as e:
        print(e)