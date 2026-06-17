def count_iterations(start, stop):
    current = start
    count = 0
    while current >= stop:
        current -= 1
        count += 1
    return count
if __name__ == '__main__':
    start_value = 100
    stop_value = 0
    iterations = count_iterations(start_value, stop_value)
    print(iterations)