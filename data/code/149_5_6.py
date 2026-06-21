def reverse_list(lst):
    return lst[::-1]

if __name__ == '__main__':
    sample_values = {'a': [10, 20, 30], 'b': [40, 50, 60]}
    reversed_values = {key: reverse_list(value) for key, value in sample_values.items()}
    print(reversed_values)