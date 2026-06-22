def validate_times(times):
    if not isinstance(times, int) or times < 1:
        raise ValueError("Times must be a positive integer")

def repeat_action(times):
    for i in range(times):
        print(f"Iteration {i + 1}")

if __name__ == '__main__':
    try:
        validate_times(10)
        repeat_action(10)
    except ValueError as e:
        print(e)