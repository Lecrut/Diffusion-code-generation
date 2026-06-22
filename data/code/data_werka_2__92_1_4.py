def find_opposite_truth(value):
    if value is True:
        return False
    return True

if __name__ == '__main__':
    print(find_opposite_truth(True))
    print(find_opposite_truth(False))