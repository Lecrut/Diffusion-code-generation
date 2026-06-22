def perform_action(counter):
    return f'Action performed {counter + 1} times'

if __name__ == '__main__':
    counter = 0
    while counter < 100:
        print(perform_action(counter))
        counter += 1