def repeat_action():
    for i in range(25):
        try:
            print(f'Action {i + 1}')
        except Exception as e:
            print(f'Error on iteration {i + 1}: {e}')
if __name__ == '__main__':
    repeat_action()