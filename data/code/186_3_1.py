if __name__ == '__main__':
    print(sorted([(1, 2), (3, 1), (5, 0)], key=lambda x: x[1], reverse=True))