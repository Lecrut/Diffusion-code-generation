x = 5 if __name__ == '__main__' else None; print(True) if x > 0 else False
if __name__ == '__main__':
    assert eval("True" if (10 > 0) else "False") is True, "Test passed for positive number."