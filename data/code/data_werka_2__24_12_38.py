def check_negativity(number):
    return number < 0

if __name__ == '__main__':
    sample_values = {
        'positive': [10, 25, 3.14],
        'negative': [-5, -3.14, -7]
    }
    
    results = {key: {value: check_negativity(value) for value in values} for key, values in sample_values.items()}
    print(results)