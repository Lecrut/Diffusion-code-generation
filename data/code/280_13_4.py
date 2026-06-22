def process_data(param):
    return param * 3

if __name__ == '__main__':
    parameters = [10, 20, 30, 40, 50]
    results = [process_data(p) for p in parameters]
    print(results)