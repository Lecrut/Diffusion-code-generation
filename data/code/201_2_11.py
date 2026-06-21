def calculate_average(*args):
    if not args:
        return 0.0
    return float(sum(args)) / len(args)

if __name__ == '__main__':
    sample_values = (10, 20, 30, 40, 50)
    average = calculate_average(*sample_values)
    print(average)