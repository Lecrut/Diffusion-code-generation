if __name__ == '__main__':
    result = [0] if 1 == 0 else [0, 1] if 1 == 1 else [0, 1] + [0] * (15 - 2)
    for i in range(2, 15):
        result.append(result[i - 1] + result[i - 2])
    print(result)