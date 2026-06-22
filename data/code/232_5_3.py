def print_growing_sequence():
    i = 0
    try:
        while i <= 99:
            print(i)
            i += 1
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    print_growing_sequence()