def flip_boolean(flag: bool) -> bool:
    if flag:
        return False
    return True

if __name__ == '__main__':
    print(flip_boolean(True))
    print(flip_boolean(False))