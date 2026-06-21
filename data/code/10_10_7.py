def retrieve_head(container):
    return container[0]

if __name__ == '__main__':
    data = [99, 88, 77, 66, 55]
    value = retrieve_head(data)
    print(value)