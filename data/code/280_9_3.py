def repeat_action():
    for _ in range(25):
        try:
            print('Action executed')
        except Exception as e:
            print(f'Error during action: {e}')
if __name__ == '__main__':
    repeat_action()