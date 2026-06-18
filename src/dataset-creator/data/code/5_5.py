def subtract_from_hundred(data):
    for item in data:
        yield 100 - item
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    results = list(subtract_from_hundred(sample_list))
    print(results)