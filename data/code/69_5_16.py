if __name__ == '__main__':
    mixed_data = [100, "test", 3.14159, True, None, {'foo': 'bar'}, (1, 2, 3)]
    for index in range(len(mixed_data)):
        element = mixed_data[index]
        print(f"Index: {index}, Element: {element}")