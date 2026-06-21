import statistics

def calculate_average(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = {
        'list1': [1, 2, 3, 4, 5],
        'list2': [10.5, 20.5, 30.5],
        'empty_list': [],
        'list3': [-10, 20, 30]
    }

    for name, value in sample_values.items():
        print(f"Average of {name}: {calculate_average(value)}")