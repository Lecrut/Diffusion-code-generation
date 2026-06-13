def running_sum_and_count(data):
    current_sum = 0
    count = 0
    for item in data:
        current_sum += item
        count += 1
        yield current_sum, count
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    results = []
    for running_sum, count in running_sum_and_count(sample_data):
        results.append((running_sum, count))
    final_sum = 0
    final_count = 0
    for running_sum, count in results:
        final_sum = running_sum
        final_count = count
    if final_count > 0:
        average = final_sum / final_count
        print(f"Final Sum: {final_sum}")
        print(f"Final Count: {final_count}")
        print(f"Average: {average}")
    else:
        print("Input data was empty.")