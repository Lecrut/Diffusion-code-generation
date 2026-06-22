MAX_ITERATIONS = 25

def execute_action():
    try:
        print('Action executed')
    except Exception as e:
        print(f'Error during action: {e}')

if __name__ == '__main__':
    for _ in range(MAX_ITERATIONS):
        execute_action()