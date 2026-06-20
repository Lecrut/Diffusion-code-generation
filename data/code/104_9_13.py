def is_before(timestamp1, timestamp2):
    return timestamp1 < timestamp2
if __name__ == '__main__':
    print(is_before(1633072800.0, 1633076400.0))
    print(is_before(1633076400.0, 1633072800.0))