def repeat_action(action, N):
    if not isinstance(N, int) or N < 0:
        raise ValueError("N must be a non-negative integer")
    
    for _ in range(N):
        action()

if __name__ == '__main__':
    def sample_action():
        print("Action executed")

    repeat_action(sample_action, 10)