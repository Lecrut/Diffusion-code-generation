counter = 0

def increment_counter():
    global counter
    counter += 1

if __name__ == '__main__':
    max_repeats = 100
    while counter < max_repeats:
        increment_counter()
    
    print(counter)