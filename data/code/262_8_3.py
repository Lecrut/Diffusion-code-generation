if __name__ == '__main__':
    data = [10, 5, 20, 3, 15]
    result = lambda lst: {'smallest': min(lst), 'largest': max(lst)}
    print(result(data))