def sum_range(start, end):
    return (end - start + 1) * (start + end) // 2

if __name__ == '__main__':
    sample_values = {
        'range_1': (1, 10),
        'range_2': (5, 15)
    }
    
    for name, (start, end) in sample_values.items():
        result = sum_range(start, end)
        print(f"The sum of numbers from {start} to {end} is: {result}")