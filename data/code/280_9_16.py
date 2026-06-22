def execute_task():
    for _ in range(25):
        try:
            perform_action()
        except Exception as e:
            print(f'Error during action: {e}')

def perform_action():
    raise ValueError("Simulated error")

if __name__ == '__main__':
    execute_task()