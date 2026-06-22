MAX_FIBONACCI_COUNT = 1000

def create_fibonacci_sequence(limit):
    current_value = 0
    next_value = 1
    items_generated = 0
    while items_generated < limit:
        yield current_value
        temp = current_value
        current_value = next_value
        next_value = temp + next_value
        items_generated += 1

def consume_and_collect(generator_function, total_items):
    collected_values = []
    raw_generator = generator_function(total_items)
    for single_item in raw_generator:
        collected_values.append(single_item)
    return collected_values

def display_summary_data(fib_list):
    start_slice = fib_list[:5]
    end_slice = fib_list[-5:]
    middle_index = len(fib_list) // 2
    middle_element = fib_list[middle_index]
    output_lines = []
    output_lines.append("First five:")
    output_lines.append(str(start_slice))
    output_lines.append("Last five:")
    output_lines.append(str(end_slice))
    output_lines.append("Middle element at index {}:".format(middle_index))
    output_lines.append(str(middle_element))
    output_lines.append("Total count:")
    output_lines.append(str(len(fib_list)))
    return output_lines

if __name__ == '__main__':
    sequence_results = consume_and_collect(create_fibonacci_sequence, MAX_FIBONACCI_COUNT)
    report_lines = display_summary_data(sequence_results)
    for line in report_lines:
        print(line)