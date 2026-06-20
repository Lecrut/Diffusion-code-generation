product_table = {1: 2, 3: 4}

def multiply(x):
    return product_table.get(x, x) * 3

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4]
    results = [multiply(value) for value in sample_values]
    print(results)