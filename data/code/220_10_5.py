import sys
def calculate_averages(data):
    results = []
    for number_set in data:
        if number_set:
            average = sum(number_set) / len(number_set)
            results.append(average)
        else:
            results.append(0)
    return results
if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [10, 20],
        [5, 5, 5, 5],
        [],
        [100]
    ]
    averages = calculate_averages(sample_data)
    for avg in averages:
        print(avg)