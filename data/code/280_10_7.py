def repeat_action(count):
    if not isinstance(count, int) or count < 0:
        raise ValueError("Count must be a non-negative integer")
    
    for _ in range(count):
        print('Repeat an action many times now')

if __name__ == '__main__':
    try:
        repeat_action(5)
    except ValueError as e:
        print(e)