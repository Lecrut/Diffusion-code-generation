if __name__ == '__main__':
    data = [(3, 1), (1, 5), (4, 2), (2, 8)]
    data.sort(key=lambda item: item[0], reverse=True)
    print(data)