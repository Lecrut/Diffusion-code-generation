def count_iterations(start, end):
    current = start
    iterations = 0
    while current >= end:
        current -= 1
        iterations += 1
    return iterations
if __name__ == '__main__':
    start_value = 100
    end_value = 0
    result = count_iterations(start_value, end_value)
    print(result)