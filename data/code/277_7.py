def count_iterations(start, end):
    count = 0
    current = start
    while current >= end:
        count += 1
        current -= 1
    return count
if __name__ == '__main__':
    start_value = 100
    end_value = 0
    result = count_iterations(start_value, end_value)
    print(result)