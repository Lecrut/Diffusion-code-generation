def execute_action():
    try:
        result = 10 / 0
        print(f'Action executed successfully: {result}')
    except ZeroDivisionError as e:
        print(f'Error during action: {e}')
if __name__ == '__main__':
    for _ in range(25):
        execute_action()