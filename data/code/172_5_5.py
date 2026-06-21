config_mapping = {
    (1, 2): "value1",
    (3, 4): "value2",
    (5, 6): "value3"
}

if __name__ == '__main__':
    print(config_mapping[(1, 2)])
    print(config_mapping[(3, 4)])
    print(config_mapping[(5, 6)])