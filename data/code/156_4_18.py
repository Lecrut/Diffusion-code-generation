def compute_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = {
        "data1": (10, 20, 30, 40, 50),
        "data2": [5, 15, 25, 35],
        "data3": (),
        "data4": [1, 2, 3]
    }
    
    for key, value in sample_values.items():
        avg = compute_average(value)
        print(f"Average of {value}: {avg}")