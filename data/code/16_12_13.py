x = 5 if __name__ == '__main__' else None; print(True) if x > 0 else False, (lambda: True)(1), (lambda: False)(-2)
if __name__ == '__main__':
    assert ((lambda _: _ > 0)(3)) is True and ((lambda _: _ > 0)(-5)) is False