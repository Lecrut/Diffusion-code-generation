if __name__ == '__main__':
    data = [15, 3, 8, 22, 1]
    result = lambda lst: {'smallest': min(lst), 'largest': max(lst)}
    print(result(data))