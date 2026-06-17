def sum_and_count(iterable):
    total = 0
    count = 0
    for item in iterable:
        total += item
        count += 1
    yield total, count
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    generator = sum_and_count(data)
    total_sum = 0
    total_count = 0
    for current_sum, current_count in generator:
        total_sum += current_sum
        total_count += current_count
    average = total_sum / total_count if total_count > 0 else 0
    print(f"The list of numbers is: {data}")
    print(f"The calculated average is: {average}")