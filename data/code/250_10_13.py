import statistics

def calculate_average(numbers):
    if not numbers:
        return 0
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = {
        'list1': [1, 2, 3, 4, 5],
        'list2': [10.5, 20.5, 30.5],
        'empty_list': [],
        'list3': [-10, 20, 30]
    }

    for key, value in sample_values.items():
        avg = calculate_average(value)
        print(f"Average of {key}: {avg}")