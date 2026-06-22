MAX_RETRIES = 25

def perform_action():
    print('Action executed')

if __name__ == '__main__':
    for _ in range(MAX_RETRIES):
        try:
            perform_action()
        except Exception as e:
            print(f'Error during action: {e}')