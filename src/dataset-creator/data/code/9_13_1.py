def calculate_running_average(data, new_value):
    data.append(new_value)
    return sum(data) / len(data)
if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    sentinel = -1
    running_sum = 0
    step = 0
    for value in sample_values:
        if value == sentinel:
            break
        running_sum += value
        current_count = len(sample_values)
        average = running_sum / current_count
        print(f"Step {step + 1}: Input {value}, Running Average: {average:.2f}")
        step += 1