def execute_action():
    print('Action executed')

def repeat_action(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Repetition factor must be a positive integer")

    for _ in range(n):
        try:
            execute_action()
        except Exception as e:
            print(f'Error during action: {e}')

if __name__ == '__main__':
    repeat_action(25)