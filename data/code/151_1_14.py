CONCATENATE = lambda list_a, list_b: [item for sublist in (list_a, list_b) for item in sublist]

if __name__ == '__main__':
    list_a = ['apple', 'banana', 'cherry']
    list_b = ['date', 'elderberry', 'fig']
    result = CONCATENATE(list_a, list_b)
    print(result)