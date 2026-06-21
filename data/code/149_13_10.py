sample_data = {
    'list': [1, 2, 3, 4, 5],
    'tuple': (6, 7, 8, 9),
    'string': "ABCDE"
}

if __name__ == '__main__':
    reversed_result = {key: list(reversed(value)) for key, value in sample_data.items()}
    print(reversed_result)