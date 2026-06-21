if __name__ == '__main__':
    data = ['cat', 'dog', 'mouse', 'cat', 'bird', 'dog']
    freq_map = {item: data.count(item) for item in set(data)}
    print(freq_map)