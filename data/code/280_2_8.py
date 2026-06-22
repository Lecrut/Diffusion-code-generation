def repeat_action(times):
    counter = 0
    while counter < times:
        print(f'Action {counter + 1} executed')
        counter += 1
if __name__ == '__main__':
    repeat_count = 100
    repeat_action(repeat_count)