def sum_sequence(start, end):
    current = start
    while current < end:
        yield current
        current += 1
if __name__ == '__main__':
    result_generator = sum_sequence(1, 10)
    total_sum = sum(result_generator)
    print(total_sum)