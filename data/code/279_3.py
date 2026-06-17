def cycle_range(start, step):
    current = start
    while current < 10:
        print(current)
        current += step
if __name__ == '__main__':
    cycle_range(0, 3)