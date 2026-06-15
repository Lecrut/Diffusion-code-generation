def running_sum_and_count(iterable):
    current_sum = 0
    count = 0
    for item in iterable:
        current_sum += item
        count += 1
        yield current_sum, count
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    result_generator = running_sum_and_count(data)
    final_sum = 0
    final_count = 0
    for current_sum, current_count in result_generator:
        final_sum = current_sum
        final_count = current_count
    if final_count > 0:
        average = final_sum / final_count
        print(f"Final Sum: {final_sum}")
        print(f"Final Count: {final_count}")
        print(f"Average: {average}")
    else:
        print("Input iterable was empty.")