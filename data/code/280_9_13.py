def execute_action():
    print('Action executed')

def repeat_action():
    for _ in range(25):
        try:
            execute_action()
        except Exception as e:
            print(f'Error during action: {e}')

if __name__ == '__main__':
    repeat_action()