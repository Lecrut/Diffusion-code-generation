def print_growing_sequence(start, end):
    i = start
    while i <= end:
        print(i)
        i += 1

if __name__ == '__main__':
    start_value = 50
    end_value = 99
    print_growing_sequence(start_value, end_value)