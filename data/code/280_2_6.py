counter = 0

def repeat_action():
    global counter
    counter += 1

if __name__ == '__main__':
    while counter < 100:
        repeat_action()
    
    print(counter)