def toggle_boolean(value: bool) -> bool:
    return bool(value ^ True)

if __name__ == '__main__':
    print(toggle_boolean(True))
    print(toggle_boolean(False))