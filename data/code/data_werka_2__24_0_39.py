def is_negative(number):
    return number < 0

if __name__ == '__main__':
    sample_values = {
        'positive': [10, 20, 30],
        'negative': [-5, -10, -15],
        'zero': [0]
    }
    
    results = {}
    for category, values in sample_values.items():
        results[category] = {value: is_negative(value) for value in values}
    
    print(results)