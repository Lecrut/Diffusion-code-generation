def calculate_average(data):
    if not data:
        return None
    total = 0
    count = 0
    for number in data:
        total += number
        count += 1
    return total / count

if __name__ == '__main__':
    sample_values = [15.2, 24.3, 33.4, 42.5, 51.6]
    avg = calculate_average(sample_values)
    print(f"Average of {sample_values}: {avg}")