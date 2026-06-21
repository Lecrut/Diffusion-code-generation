def calculate_average(*args):
    if not args:
        return 0.0
    return sum(args) / len(args)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    average_result = calculate_average(*sample_values)
    print(f"The average is: {average_result:.2f}")