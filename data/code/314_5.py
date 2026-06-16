def running_total_generator(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result_generator = running_total_generator(data)
    running_totals = list(result_generator)
    print(running_totals)