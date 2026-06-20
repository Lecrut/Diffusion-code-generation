def check_equal():
    sample_values = {'value1': 20, 'value2': 20}
    return sample_values['value1'] == sample_values['value2']

if __name__ == '__main__':
    result = check_equal()
    print(result)