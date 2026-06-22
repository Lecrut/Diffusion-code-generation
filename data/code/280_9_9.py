def perform_action():
    try:
        result = 10 / (5 - 4)
        print(f'Action performed with result: {result}')
    except Exception as e:
        print(f'Error during action: {e}')
if __name__ == '__main__':
    for _ in range(25):
        perform_action()