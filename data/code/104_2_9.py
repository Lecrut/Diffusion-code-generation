def time_difference(timestamp1, timestamp2):
    return abs(timestamp1 - timestamp2)

if __name__ == '__main__':
    result = time_difference(1633072800, 1633072860)
    print(result)