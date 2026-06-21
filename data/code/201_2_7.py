def calculate_average(*args):
    if not args:
        return 0.0
    return sum(args) / len(args)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    average = calculate_average(*sample_data)
    print(average)