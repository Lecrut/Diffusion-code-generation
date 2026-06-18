def calculate_running_average(data):
    return sum(data) / len(data) if data else 0
if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    sentinel = -1
    running_sum = 0
    step = 0
    for value in sample_values:
        if value == sentinel:
            break
        running_sum += value
        step += 1
        current_average = running_sum / step
        print(f"Step {step}: Current Value = {value}, Running Average = {current_average:.2f}")