MAX_ITERATIONS = 25

def perform_action():
    print('Action executed')

def repeat_action_with_error_handling(n):
    for _ in range(n):
        try:
            perform_action()
        except Exception as e:
            print(f'Error during action: {e}')

if __name__ == '__main__':
    repeat_action_with_error_handling(MAX_ITERATIONS)