def running_sum_count_generator(data):
    running_sum = 0
    count = 0
    first_element_sum = 0
    first_element_count = 0
    second_element_sum = 0
    second_element_count = 0
    for i, pair in enumerate(data):
        running_sum += pair[0]
        count += 1
        if count == 1:
            first_element_sum = running_sum
            first_element_count = count
        elif count == 2:
            second_element_sum = running_sum
            second_element_count = count
    yield first_element_sum, first_element_count
    yield second_element_sum, second_element_count
if __name__ == '__main__':
    sample_data = [(10, 5), (20, 8), (30, 12)]
    results = running_sum_count_generator(sample_data)
    print("First element results:")
    for sum_val, count in results:
        average = sum_val / count if count > 0 else 0
        print(f"Sum: {sum_val}, Count: {count}, Average: {average}")
    print("\nSecond element results:")
    for sum_val, count in results:
        average = sum_val / count if count > 0 else 0
        print(f"Sum: {sum_val}, Count: {count}, Average: {average}")