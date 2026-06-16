def cycle_processor(lower_bound, upper_bound):
    results = []
    for number in range(lower_bound, upper_bound + 1):
        results.append(number)
    return results
if __name__ == '__main__':
    lower = 5
    upper = 10
    output = cycle_processor(lower, upper)
    print(output)