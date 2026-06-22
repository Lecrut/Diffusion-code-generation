def repeat_action(times):
    if times < 1:
        raise ValueError("Times must be a positive integer")
    for i in range(times):
        print(f"Iteration {i + 1}")

if __name__ == '__main__':
    try:
        repeat_action(10)
    except ValueError as e:
        print(e)