if __name__ == '__main__':
    data = [(3, 1), (1, 0), (4, 2), (2, 3)]
    data.sort(key=lambda x: x[0], reverse=True)
    print(data)