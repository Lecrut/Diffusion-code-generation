import statistics

def calculate_average(numbers):
    if not numbers:
        return 0
    try:
        return statistics.mean(numbers)
    except TypeError:
        raise ValueError("All elements in the list must be numbers")

if __name__ == '__main__':
    sample_values = {
        'list1': [1, 2, 3, 4, 5],
        'list2': [10.5, 20.5, 30.5],
        'empty_list': [],
        'list3': [-10, 20, 30]
    }
    for name, value in sample_values.items():
        try:
            print(f"Average of {name}: {calculate_average(value)}")
        except ValueError as e:
            print(e)