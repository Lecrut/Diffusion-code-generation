def evaluate_number(value):
    if value > 0:
        return 'Positive'
    elif value < 0:
        return 'Negative'
    else:
        return 'Zero'

if __name__ == '__main__':
    sample_values = [25, -10, 0]
    for val in sample_values:
        result = evaluate_number(val)
        print(f'The number {val} is {result}.')