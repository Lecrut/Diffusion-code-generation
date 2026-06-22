def process_data(param):
    return param.upper()

if __name__ == '__main__':
    data = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    results = [process_data(d) for d in data]
    print(results)