def get_opposite_truth_value(value):
    truth_values = {'True': False, 'False': True}
    return truth_values.get(value, None)

if __name__ == '__main__':
    sample1 = 'True'
    opposite1 = get_opposite_truth_value(sample1)
    print(f"Original: {sample1}, Opposite: {opposite1}")
    sample2 = 'False'
    opposite2 = get_opposite_truth_value(sample2)
    print(f"Original: {sample2}, Opposite: {opposite2}")