def filter_positive(data):
    return (x for x in data if x >= 0)
if __name__ == '__main__':
    stream = [-5, -1, 0, 3, 7, -2]
    filtered_stream = list(filter_positive(stream))