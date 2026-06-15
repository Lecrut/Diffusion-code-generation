def element_sum_count(iterable):
    total = 0
    count = 0
    for item in iterable:
        total += item
        count += 1
    yield total, count
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    generator = element_sum_count(sample_data)
    total_sum = 0
    element_count = 0
    for current_sum, current_count in generator:
        total_sum = current_sum
        element_count = current_count
    if element_count > 0:
        mean = total_sum / element_count
        print(f"Sum: {total_sum}")
        print(f"Count: {element_count}")
        print(f"Mean: {mean}")
    else:
        print("The iterable is empty")