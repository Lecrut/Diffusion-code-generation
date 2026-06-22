def print_growing_sequence():
    i = 0
    while True:
        if i > 99:
            break
        print(i)
        i += 1

if __name__ == '__main__':
    try:
        print_growing_sequence()
    except Exception as e:
        print(f"An error occurred: {e}")