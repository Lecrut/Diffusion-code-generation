product_table = {2: lambda x: x * 2}

if __name__ == '__main__':
    sample_value = 3
    result = product_table[2](sample_value)
    print(result)