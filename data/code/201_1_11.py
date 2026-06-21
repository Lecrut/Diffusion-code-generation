import statistics

def compute_average(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = {
        'list1': [5, 10, 15, 20, 25],
        'list2': [3.5, 7.5, 11.5, 15.5, 19.5],
        'empty_list': [],
        'list3': [-5, 0, 5, 10]
    }
    for name, value in sample_values.items():
        print(f"Average of {name}: {compute_average(value)}")