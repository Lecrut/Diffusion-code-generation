def repeat_action():
    for _ in range(25):
        try:
            if random.choice([True, False]):
                raise Exception('Random error occurred')
            print('Action executed')
        except Exception as e:
            print(f'Error during action: {e}')
if __name__ == '__main__':
    import random
    repeat_action()