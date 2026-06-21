def calculate_average(data):
    if not data:
        return None
    total = sum(data)
    count = len(data)
    return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    avg = calculate_average(sample_values)
    print(f"Average of {sample_values}: {avg}")