def calculate_running_average(data):
    return sum(data) / len(data) if data else 0
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    sentinel = -1
    running_average = 0.0
    for number in sample_data:
        if number == sentinel:
            break
        running_average += number
        current_count = len(sample_data)
        if current_count > 0:
            running_average = running_average / current_count
        print(f"Input: {number}, Running Average: {running_average}")